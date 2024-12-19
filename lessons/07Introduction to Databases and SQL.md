
# **Lesson 07 — Introduction to Databases and SQL**

## **Lesson Overview**
**Learning objective:** Students will gain foundational knowledge of databases and SQL by learning to create, populate, and query a SQLite database using Python. They will also understand how to manage database connections and commit changes.

---

## **7.1 Setting Up the Environment**

### **Overview**
To work with databases in Python, you need a few tools installed and properly configured.

### **Steps:**
1. **Install Python**  
   - Download and install Python from [python.org](https://www.python.org/). Verify installation by running:
     ```bash
     python --version
     ```

2. **Set Up a Code Editor**  
   - Install a code editor such as Visual Studio Code or PyCharm.

3. **Verify SQLite Installation**  
   - SQLite comes pre-installed with Python. Check by running:
     ```python
     import sqlite3
     print(sqlite3.version)
     ```

### **Tips:**
- Use `pip install` to install additional libraries if needed.
- Use a dedicated folder for your project files.

---

## **7.2 Creating a New SQLite Database**

### **Overview**
SQLite is a lightweight, file-based database. You can create and interact with an SQLite database using Python's `sqlite3` library.

### **Steps to Create a Database:**
1. Open your code editor and create a new Python script file (e.g., `lesson07.py`).
2. Use the `sqlite3.connect()` method to connect to a new database. SQLite automatically creates the database file if it does not exist.

### **Example Code:**
```python
import sqlite3

# Connect to a new SQLite database
conn = sqlite3.connect("school.db")

# Verify connection
print("Database created and connected successfully.")

# Close the connection
conn.close()
```

### **Outcome:**
Running the script creates a `school.db` file in the project folder.

---

## **7.3 Defining the Database Structure**

### **Overview**
Databases use tables to store structured data. SQL queries are used to define the table schema.

### **Steps:**
1. Use SQL `CREATE TABLE` queries to define the structure of your database.
2. Execute these queries within your Python script using the `execute()` method of a database cursor.

### **Tables:**
- `Students`: Contains `student_id`, `name`, `age`, and `major`.
- `Courses`: Contains `course_id`, `course_name`, and `instructor_name`.
- `Enrollments`: Contains `enrollment_id`, `student_id`, and `course_id`.

### **Example Code:**
```python
# Connect to the database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    major TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    instructor_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES Students (student_id),
    FOREIGN KEY (course_id) REFERENCES Courses (course_id)
)
""")

print("Tables created successfully.")
conn.close()
```

---

## **7.4 Populating Tables with Data**

### **Overview**
Insert sample data into tables to practice running queries.

### **Steps:**
1. Use SQL `INSERT INTO` queries to add data to the tables.
2. Execute the queries within your Python script.

### **Example Code:**
```python
# Connect to the database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Insert sample data into tables
cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science')")
cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Smith')")
cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (1, 1)")

conn.commit()
print("Sample data inserted successfully.")
conn.close()
```

---

## **7.5 Writing SQL Queries**

### **Overview**
Retrieve and analyze data using SQL queries.

### **Queries:**
1. Retrieve all student information:
   ```sql
   SELECT * FROM Students;
   ```

2. Find courses taught by a specific instructor:
   ```sql
   SELECT * FROM Courses WHERE instructor_name = 'Dr. Smith';
   ```

3. Retrieve student enrollments with course names using a `JOIN`:
   ```sql
   SELECT Students.name, Courses.course_name 
   FROM Enrollments
   JOIN Students ON Enrollments.student_id = Students.student_id
   JOIN Courses ON Enrollments.course_id = Courses.course_id;
   ```

4. List students ordered by age:
   ```sql
   SELECT * FROM Students ORDER BY age;
   ```

### **Example Code:**
```python
# Connect to the database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Execute and display query results
cursor.execute("SELECT * FROM Students")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Courses WHERE instructor_name = 'Dr. Smith'")
print(cursor.fetchall())

conn.close()
```

---

## **7.6 Committing Changes and Finalizing**

### **Overview**
Ensure all database operations are saved and the connection is properly closed.

### **Steps:**
1. Use `conn.commit()` to save changes.
2. Use `conn.close()` to close the connection.

### **Example Code:**
```python
# Save changes and close connection
conn.commit()
conn.close()
print("Database operations finalized.")
```

---

## **Summary**

In this lesson, you learned:
1. How to create and connect to an SQLite database.
2. How to define tables using SQL queries.
3. How to populate tables with sample data.
4. How to write SQL queries to retrieve and analyze data.
5. How to commit changes and close the database connection.

For further exploration, refer to the [SQLite Documentation](https://www.sqlite.org/docs.html) and Python’s `sqlite3` library documentation.
```
