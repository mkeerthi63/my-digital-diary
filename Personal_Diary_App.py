import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
from datetime import datetime
# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("diary.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT,
    content TEXT,
    date TEXT
)
""")
conn.commit()
# ---------------- PASSWORD HASH FUNCTION ----------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
# ---------------- MAIN APP ----------------
class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Diary App")
        self.root.geometry("700x600")
        self.current_user_id = None
        self.login_screen()
    # ---------------- LOGIN SCREEN ----------------
    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Login", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register).pack()
    def login(self):
        username = self.username_entry.get()
        password = hash_password(self.password_entry.get())
        cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()

        if result:
            self.current_user_id = result[0]
            self.main_screen()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    def register(self):
        username = self.username_entry.get()
        password = hash_password(self.password_entry.get())

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration Successful!")
        except:
            messagebox.showerror("Error", "Username already exists")

    # ---------------- MAIN DIARY SCREEN ----------------
    def main_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="My Diary", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(self.root, text="Title").pack()
        self.title_entry = tk.Entry(self.root, width=50)
        self.title_entry.pack()

        self.text_area = tk.Text(self.root, height=15)
        self.text_area.pack(pady=10)

        tk.Button(self.root, text="Save Entry", command=self.save_entry).pack(pady=5)
        tk.Button(self.root, text="View Entries", command=self.view_entries).pack()
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=5)

    def save_entry(self):
        title = self.title_entry.get()
        content = self.text_area.get("1.0", tk.END).strip()
        date = datetime.now().strftime("%Y-%m-%d %H:%M")

        if not title or not content:
            messagebox.showerror("Error", "Title and Content required")
            return

        cursor.execute(
            "INSERT INTO entries (user_id, title, content, date) VALUES (?, ?, ?, ?)",
            (self.current_user_id, title, content, date)
        )
        conn.commit()

        messagebox.showinfo("Success", "Entry Saved!")
        self.title_entry.delete(0, tk.END)
        self.text_area.delete("1.0", tk.END)

    def view_entries(self):
        self.clear_screen()

        tk.Label(self.root, text="Your Entries", font=("Arial", 18, "bold")).pack(pady=10)

        cursor.execute("SELECT id, title, date FROM entries WHERE user_id=?", (self.current_user_id,))
        entries = cursor.fetchall()

        self.entry_list = tk.Listbox(self.root, width=80)
        self.entry_list.pack(pady=10)

        for entry in entries:
            self.entry_list.insert(tk.END, f"{entry[0]} | {entry[1]} | {entry[2]}")

        tk.Button(self.root, text="Open Entry", command=self.open_entry).pack()
        tk.Button(self.root, text="Delete Entry", command=self.delete_entry).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_screen).pack()

    def open_entry(self):
        selected = self.entry_list.get(tk.ACTIVE)
        entry_id = selected.split("|")[0].strip()

        cursor.execute("SELECT title, content FROM entries WHERE id=?", (entry_id,))
        entry = cursor.fetchone()

        self.clear_screen()

        tk.Label(self.root, text=entry[0], font=("Arial", 16, "bold")).pack(pady=10)
        text = tk.Text(self.root, height=20)
        text.pack()
        text.insert(tk.END, entry[1])
        text.config(state="disabled")

        tk.Button(self.root, text="Back", command=self.view_entries).pack(pady=5)

    def delete_entry(self):
        selected = self.entry_list.get(tk.ACTIVE)
        entry_id = selected.split("|")[0].strip()

        cursor.execute("DELETE FROM entries WHERE id=?", (entry_id,))
        conn.commit()

        messagebox.showinfo("Deleted", "Entry deleted successfully")
        self.view_entries()

    # ---------------- UTILITY ----------------
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ---------------- RUN APP ----------------
root = tk.Tk()
app = DiaryApp(root)
root.mainloop()