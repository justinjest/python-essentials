
# **Lesson 10 — Data Storage and Retrieval**

## **Lesson Overview**
**Learning objective:** Students will learn to store and retrieve data efficiently using JSON, CSV, and databases. They will also explore how to manipulate and analyze stored data using Python libraries and compare storage optimization strategies for different project scales.

### **Topics:**
1. Storing Scraped Data: JSON, CSV, and Databases
2. Retrieving and Analyzing Data: SQL and Pandas
3. Optimizing Data Storage: Relational vs. Non-relational Databases

---

## **10.1 Storing Scraped Data**

### **Overview**
Storing scraped data ensures it can be reused or analyzed later. Common storage formats include:
- **JSON:** A lightweight format for structured data.
- **CSV:** A tabular format, easily readable in spreadsheets.
- **Databases:** Ideal for complex, structured data.

### **Storing Data in JSON**
1. Use Python's `json` module to save data in a structured format.
2. Store scraped elements like page titles, headers, and links.

#### **Example Code: Storing Data in JSON**
```python
import json

# Sample scraped data
data = {
    "title": "Web scraping",
    "headers": ["Introduction", "Techniques", "Legal issues"],
    "links": ["https://example.com/intro", "https://example.com/techniques"]
}

# Save data to a JSON file
with open("scraped_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data saved to scraped_data.json.")
```

---

### **Storing Data in CSV**
1. Use Python's `csv` module to write data in rows and columns.
2. Add more details like image sources or descriptions.

#### **Example Code: Storing Data in CSV**
```python
import csv

# Sample scraped data
data = [
    ["Header", "Link", "Image"],
    ["Introduction", "https://example.com/intro", "https://example.com/image1.png"],
    ["Techniques", "https://example.com/techniques", "https://example.com/image2.png"]
]

# Save data to a CSV file
with open("scraped_data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

print("Data saved to scraped_data.csv.")
```

---

### **Storing Data in Databases**
1. Use SQLite to create a database table.
2. Insert scraped data using SQL commands.

#### **Example Code: Storing Data in a Database**
```python
import sqlite3

# Connect to the database
conn = sqlite3.connect("scraped_data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS ScrapedData (
    id INTEGER PRIMARY KEY,
    header TEXT,
    link TEXT,
    image TEXT
)
""")

# Insert sample data
cursor.execute("INSERT INTO ScrapedData (header, link, image) VALUES (?, ?, ?)",
               ("Introduction", "https://example.com/intro", "https://example.com/image1.png"))
conn.commit()

print("Data saved to the database.")
conn.close()
```

---

## **10.2 Retrieving and Analyzing Data**

### **Overview**
Retrieve and manipulate stored data using Python libraries like `Pandas` and SQL queries. Analyze the data for insights such as counts or patterns.

#### **Example Code: Retrieving Data into a Pandas DataFrame**
```python
import pandas as pd

# Connect to the database and load data into a DataFrame
conn = sqlite3.connect("scraped_data.db")
query = "SELECT * FROM ScrapedData"
df = pd.read_sql_query(query, conn)

# Perform analyses
header_count = len(df['header'].unique())
link_count = len(df['link'].unique())

print(f"Number of unique headers: {header_count}")
print(f"Number of unique links: {link_count}")

conn.close()
```

---

## **10.3 Optimizing Data Storage**

### **Overview**
Choosing the right storage type depends on the scale and complexity of the project.

### **Comparison: Relational vs. Non-relational Databases**
| Feature               | Relational (e.g., SQLite) | Non-relational (e.g., MongoDB) |
|-----------------------|--------------------------|--------------------------------|
| Data Structure        | Tables with rows/columns | Flexible document structure    |
| Query Language        | SQL                     | NoSQL or JSON-based queries    |
| Scalability           | Limited for large data  | High scalability               |
| Best Use Case         | Structured, small-scale | Unstructured, large-scale      |

### **Key Points:**
- **Relational Databases:** Ideal for small-scale projects like scraping Wikipedia, where data is structured and relationships are simple.
- **Non-relational Databases:** Better suited for large-scale projects with high-volume, semi-structured, or unstructured data.

---

## **Summary**

In this lesson, you learned:
1. How to store data in JSON, CSV, and databases.
2. How to retrieve and analyze stored data using SQL and Pandas.
3. The differences between relational and non-relational databases and their appropriate use cases.

For further reading, explore the [Python JSON Documentation](https://docs.python.org/3/library/json.html), [SQLite Documentation](https://www.sqlite.org/docs.html), and [Pandas Documentation](https://pandas.pydata.org/docs/).
