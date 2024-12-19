
# **Lesson 06 — Data Cleaning and Validation with Pandas**

## **Lesson Overview**
**Learning objective:** Students will learn to apply fundamental data cleaning and validation techniques using Pandas. These include handling missing data, transforming data types, removing duplicates, managing outliers, standardizing text data, and validating data ranges.

### **Topics:**
1. Handling Missing Data
2. Data Transformation
3. Removing Duplicates
4. Handling Outliers
5. Standardizing Data
6. Validating Data Ranges

---

## **6.1 Handling Missing Data**

### **Overview**
Missing data can affect the accuracy and reliability of analysis. Common approaches include removing or replacing missing values.

### **Key Methods:**
- `dropna()`: Removes rows or columns with missing values.
- `fillna()`: Replaces missing values with specified replacements like the mean, median, or a default value.

### **Why Handle Missing Data?**
- Ensures consistent dataset formatting.
- Avoids errors during calculations.
- Preserves data integrity.

### **Code Example:**
```python
import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', None, 'Charlie', 'David'],
        'Age': [24, None, 22, 35],
        'Salary': [50000, 60000, None, None]}
df = pd.DataFrame(data)

# Drop rows with missing data
df_dropped = df.dropna()

# Replace missing values
df_filled = df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'Salary': 0})

print("DataFrame with missing data handled:")
print(df_filled)
```

---

## **6.2 Data Transformation**

### **Overview**
Data transformation converts data into consistent formats and types for easier analysis and calculations.

### **Key Tasks:**
- Converting data types.
- Formatting date columns for temporal analysis.

### **Why Transform Data?**
- Ensures compatibility with numerical and time-based functions.
- Reduces inconsistencies in datasets.

### **Code Example:**
```python
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': ['24', '27', '22'],
        'Join_Date': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)

# Convert 'Age' to integer
df['Age'] = df['Age'].astype(int)

# Convert 'Join_Date' to datetime
df['Join_Date'] = pd.to_datetime(df['Join_Date'])

print("Transformed DataFrame:")
print(df)
```

---

## **6.3 Removing Duplicates**

### **Overview**
Duplicates can distort analysis by inflating metrics or introducing bias. Identifying and removing them ensures data quality.

### **Key Method:**
- `duplicated()`: Identifies duplicates.
- `drop_duplicates()`: Removes duplicate rows.

### **Code Example:**
```python
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [24, 27, 24, 35],
        'Salary': [50000, 60000, 50000, 80000]}
df = pd.DataFrame(data)

# Remove duplicates
df_no_duplicates = df.drop_duplicates()

print("DataFrame with duplicates removed:")
print(df_no_duplicates)
```

---

## **6.4 Handling Outliers**

### **Overview**
Outliers are extreme values that deviate significantly from other observations and can bias statistical calculations.

### **Common Approach:**
- Replace outliers with statistical measures like the median.

### **Code Example:**
```python
# Replace outliers in 'Age' (e.g., Age > 100 or Age < 0)
df['Age'] = df['Age'].apply(lambda x: df['Age'].median() if x > 100 or x < 0 else x)

print("DataFrame after handling outliers:")
print(df)
```

---

## **6.5 Standardizing Data**

### **Overview**
Standardizing text data ensures consistency, making it easier to group, filter, and analyze.

### **Key Techniques:**
- Convert text to lowercase and strip whitespace.
- Standardize inconsistent entries.

### **Code Example:**
```python
# Standardize 'Name' column
df['Name'] = df['Name'].str.lower().str.strip()

# Standardize 'City' column with mapping
df['City'] = df['City'].replace({'ny': 'New York', 'la': 'Los Angeles'})

print("Standardized DataFrame:")
print(df)
```

---

## **6.6 Validating Data Ranges**

### **Overview**
Validating data ranges ensures all values fall within acceptable limits, avoiding invalid or erroneous data.

### **Example Task:**
- Ensure ages are between 18 and 65. Replace invalid values with `NaN` and fill them with the median.

### **Code Example:**
```python
# Replace invalid ages with NaN
df['Age'] = df['Age'].apply(lambda x: x if 18 <= x <= 65 else None)

# Fill missing values with median
df['Age'] = df['Age'].fillna(df['Age'].median())

print("DataFrame after validating age ranges:")
print(df)
```

---

## **Summary**

In this lesson, you learned how to:
1. Handle missing data with `dropna()` and `fillna()`.
2. Transform data types and formats.
3. Remove duplicate records.
4. Identify and manage outliers.
5. Standardize text data for consistency.
6. Validate data ranges to ensure accuracy.

These techniques are essential for maintaining clean, reliable datasets, ready for analysis. Explore the [Pandas Documentation](https://pandas.pydata.org/docs/) to deepen your understanding.
```

