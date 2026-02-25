# 📝 My Digital Diary (Python GUI)

A secure and user-friendly personal diary application built with Python, Tkinter, and SQLite.  
This desktop app lets users register, log in, and manage personal diary entries in a structured and private environment.

---

## 🚀 Features

- 🔐 User Registration & Login
- 🔒 Password Hashing (SHA-256)
- 📝 Create Diary Entries with Title, Content, & Timestamp
- 📂 View All Saved Entries
- ❌ Delete Entries
- 🗄 Stores Data in SQLite Database
- 👤 User-Specific Data Separation

---

## 🛠 Tech Stack

- Python
- Tkinter (GUI)
- SQLite (Database)
- Hashlib (Password Security)

---

## 📂 Project Structure

```

my-digital-diary/
│
├── diary.db                # SQLite database (not included)
├── main.py                 # Main application code
└── README.md               # Documentation

```

---

## 🗄 Database Schema

### **Users Table**

| Column   | Type                |
|----------|---------------------|
| id       | INTEGER (Primary Key) |
| username | TEXT (Unique)          |
| password | TEXT (Hashed SHA-256) |

### **Entries Table**

| Column   | Type                |
|----------|---------------------|
| id       | INTEGER (Primary Key) |
| user_id  | INTEGER (Foreign Key) |
| title    | TEXT                  |
| content  | TEXT                  |
| date     | TEXT                  |

---

## ▶️ How to Run

1. **Install Python 3.x**  
2. Clone your repository:

```

git clone [https://github.com/mkeerthi63/my-digital-diary.git](https://github.com/mkeerthi63/my-digital-diary.git)

```

3. Navigate into the project directory:

```

cd my-digital-diary

```

4. Run the application:

```

python main.py

```

---

## 📌 Usage

1. Register a new user with a unique username and password  
2. Log in with your credentials  
3. Create new diary entries  
4. View and delete previously saved entries

---

## 💡 What You’ll Learn

- Event-driven GUI development with Tkinter  
- User authentication + password security  
- Using SQLite for structured data storage  
- Building a real-world desktop application

---

## 📌 Future Enhancements

- 🖊️ Add Edit Entry functionality  
- 🔎 Search entries by title or keyword  
- 🌓 Dark mode UI option  
- 📑 Export entries as PDF  
- 🔐 Optional encryption for saved content

---

## 📄 Summary for Resume

Built a desktop diary application using Python and Tkinter with secure user login and SQLite for structured diary storage. Added CRUD operations and password hashing to demonstrate secure data handling and practical GUI application design.

---

## 👨‍💻 Author

**M. Keerthi**  
GitHub: [mkeerthi63](https://github.com/mkeerthi63)
```

