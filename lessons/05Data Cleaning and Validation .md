# Lesson 05 — Data Cleaning and Validation I

## Lesson Overview

**Learning objective:** Students will learn techniques for handling missing data, transforming data types, and identifying and removing duplicate records to ensure data quality.

### Topics
1. Handling Missing Data: Removing rows with `dropna()`, replacing values with `fillna()`.
2. Data Transformation: Converting data types, reformatting dates.
3. Removing Duplicates: Identifying and removing duplicate records.

---

## 5.1 Handling Missing Data

### Overview
Missing data can cause errors or inaccuracies in analysis. Pandas provides methods to handle missing data by removing rows or replacing missing values.

### Key Methods
- `dropna()`: Removes rows or columns with missing data.
- `fillna()`: Replaces missing data with specified values.

### Why Handle Missing Data?
- Ensures accurate calculations and visualizations.
- Prevents runtime errors during analysis.
- Allows consistent dataset formatting.

### Example: Using `dropna()` and `fillna()`
```python
import pandas as pd

# Sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', None, 'David'],
        'Age': [24, 27, 22, None],
        'Score': [85, None, 88, 76]}
df = pd.DataFrame(data)

# Remove rows with missing data
df_dropped = df.dropna()
print(df_dropped)

# Replace missing data with default values
df_filled = df.fillna({'Age': 0, 'Score': df['Score'].mean()})
print(df_filled)
```

---

## 5.2 Data Transformation

### Overview
Data transformation ensures consistency in data types and formats, making the dataset ready for analysis or visualization.

### Key Tasks
- Converting data types (e.g., strings to integers).
- Reformatting date strings into `datetime` objects.

### Why Transform Data?
- Prevents errors due to mismatched data types.
- Simplifies operations such as comparisons and calculations.
- Ensures uniformity in dataset representation.

### Example: Converting Data Types and Reformatting Dates
```python
# Sample DataFrame with mixed data types
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': ['24', '27', '22'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)

# Convert 'Age' column to integers
df['Age'] = df['Age'].astype(int)

# Convert 'JoinDate' column to datetime
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df.dtypes)  # Verify data types
print(df)
```

---

## 5.3 Removing Duplicates

### Overview
Duplicate records can skew results and inflate metrics. Pandas provides methods to identify and remove duplicate rows.

### Key Method
- `drop_duplicates()`: Removes duplicate rows based on one or more columns.

### Why Remove Duplicates?
- Prevents redundant information in analysis.
- Improves data quality and storage efficiency.
- Ensures unique data for accurate insights.

### Example: Using `drop_duplicates()`
```python
# Sample DataFrame with duplicates
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [24, 27, 24, 32],
        'Score': [85, 92, 85, 76]}
df = pd.DataFrame(data)

# Identify and remove duplicates
df_cleaned = df.drop_duplicates()
print(df_cleaned)

# Remove duplicates based on 'Name' column
df_cleaned_by_name = df.drop_duplicates(subset='Name')
print(df_cleaned_by_name)
```

---

## Check for Understanding

1. **Which method removes rows with missing values?**
   - A) `fillna()`
   - B) `dropna()`
   - C) `remove_missing()`
   - D) `replace_na()`

2. **How do you convert a column of strings to integers?**
   - A) `pd.to_int(column)`
   - B) `df['column'].convert(int)`
   - C) `df['column'].astype(int)`
   - D) `df['column'].to_int()`

3. **Which method is used to remove duplicate rows in Pandas?**
   - A) `remove_duplicates()`
   - B) `drop_duplicates()`
   - C) `find_duplicates()`
   - D) `remove_redundant()`

### Answer Key
1. B  
2. C  
3. B  

---

## Summary

In this lesson, you’ve learned:
- How to handle missing data using `dropna()` and `fillna()`.
- How to transform data by converting data types and reformatting dates.
- How to identify and remove duplicate records with `drop_duplicates()`.

By applying these techniques, you can clean and validate your datasets for accurate and effective analysis. For further exploration, refer to the [Pandas Documentation](https://pandas.pydata.org/docs/) and Python's [official documentation](https://docs.python.org/3/).
