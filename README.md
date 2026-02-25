# 📝 Secure Personal Diary Application (Python GUI)

A secure desktop-based Personal Diary application built using Python, Tkinter, and SQLite.  
This application allows users to register, log in, and manage personal diary entries securely.

---

## 🚀 Features

- 🔐 User Registration & Login System
- 🔒 Password Hashing (SHA-256)
- 📝 Create Diary Entries (Title + Content + Date)
- 📂 View All Saved Entries
- ❌ Delete Entries
- 🗄 SQLite Database Integration
- 👤 User-Specific Data Storage

---

## 🛠 Tech Stack

- Python
- Tkinter (GUI)
- SQLite (Database)
- Hashlib (Password Security)

---

## 📂 Project Structure

```
secure-personal-diary-app/
│
├── diary.db
├── main.py
└── README.md
```

---

## 🗄 Database Schema

### Users Table
| Column   | Type    |
|----------|---------|
| id       | INTEGER (Primary Key) |
| username | TEXT (Unique) |
| password | TEXT (Hashed) |

### Entries Table
| Column   | Type    |
|----------|---------|
| id       | INTEGER (Primary Key) |
| user_id  | INTEGER (Foreign Key) |
| title    | TEXT |
| content  | TEXT |
| date     | TEXT |

---

## ▶️ How to Run

1. Install Python (3.x recommended)
2. Clone this repository:

```
git clone https://github.com/your-username/secure-personal-diary-app.git
```

3. Navigate to project folder:

```
cd secure-personal-diary-app
```

4. Run the application:

```
python main.py
```

---

## 🎯 Learning Outcomes

- Event-driven GUI programming
- User authentication implementation
- Password hashing for security
- SQLite database integration
- CRUD operations (Create, Read, Delete)

---
## 📌 Future Improvements

- Edit entry feature
- Search functionality
- Dark mode
- Export to PDF
- Entry encryption
- Cloud backup integration

---

## 📄 Resume Description

Developed a secure desktop diary application using Python and Tkinter. Implemented user authentication with password hashing and integrated SQLite database for structured diary entry storage. Designed CRUD operations with a responsive graphical interface.

---

## 👨‍💻 Author

Your Name
