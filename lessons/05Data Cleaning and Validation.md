
## Lesson 05 — Data Cleaning and Validation I

**Lesson Overview**

**Learning objective:** Students will learn techniques for handling missing data, transforming data types, and identifying and removing duplicate records to ensure data quality. This lesson will provide foundational skills necessary for cleaning raw data, ensuring it's ready for effective analysis.

### Topics

1. **Handling Missing Data**: Removing rows with `dropna()`, replacing values with `fillna()`.
2. **Data Transformation**: Converting data types, reformatting dates, **feature engineering**, **data discretization**.
3. **Removing Duplicates**: Identifying and removing duplicate records.
4. **Removing Outliers**: Identify and removing outling records
---

## 5.1 Handling Missing Data

### Overview

Missing data is common in datasets and can significantly affect the outcome of analyses if not handled properly. In Pandas, there are methods to identify and handle missing data, either by removing rows or by filling in the missing values. Correctly managing missing data is crucial for ensuring accurate results.

### Key Methods

- `dropna()`: Removes rows or columns with missing data.
- `fillna()`: Replaces missing values with specified values.

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

**Explanation:**

`dropna()` removes any row that contains a `None` (missing) value. This can remove quite a lot of data, especially if you have a lot of columns.

`fillna()` is used to replace missing values. In this case, the `Age` column's missing values are replaced with 0, and the `Score` column's missing values are filled with the mean of the existing scores. This can cause issues if the values you are replacing become outliers.

## 5.2 Data Transformation

### Overview

Data transformation is essential for ensuring that all data conforms to the correct format and type, which makes it easier to manipulate and analyze. This includes tasks like converting strings to numeric values, reformatting date strings into datetime objects, **creating new features** (feature engineering), and **discretizing continuous variables**.

### Key Tasks

- Converting data types (e.g., strings to integers).
- Reformatting date strings into datetime objects.
- **Creating new features:** 
    - Combining existing features (e.g., `Age` and `YearsOfExperience` to create `AgeGroup`).
    - Extracting features from existing ones (e.g., extracting `Year` and `Month` from a `Date` column).
    - Generating interaction features (e.g., multiplying two features).
- **Data Discretization:** 
    - Binning continuous variables into discrete categories (e.g., age ranges, income brackets).
    - Using techniques like `pd.cut()` or `pd.qcut()`.

### Why Transform Data?

- Prevents errors due to mismatched data types.
- Simplifies operations such as comparisons and calculations.
- Ensures uniformity in dataset representation.
- Improves model performance in machine learning tasks.

### Example: Converting Data Types and Reformatting Dates

```python
import pandas as pd

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
In addition you can use pandas.DataFrame.map we can change items in a column. A possible pitfall with this method is that it will only work if you define a replacement for all items in the column.
```python
import pandas as pd

# Sample DataFrame with age in days

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)

# Convert 'Location' abbreviations into full names

df['Location'] = df['Location'].map({'LA': 'Los Angeles', 'NY': "New York"})
print(df)
```

This method is useful when you want to replace everything in one column due to abreviation, and you know what the data will be beforehand.

For **Data Discretization** we have to use the more complicated pandas.cut() function. This will allow us to automatically split data into a series of equal sized bins.

```python
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'Grade': [78, 40, 85]}
df = pd.DataFrame(data)

# Convert grade into three catagories, "bad", "okay", "great"

df['Grade'] = pd.cut(df['Grade'], 3, labels = ["bad", "okay", "great"])
print(df)
```

**Explanation:**

`astype(int)` converts the `Age` column, originally stored as strings, into integers.
`pd.to_datetime()` converts the `JoinDate` column into Python’s datetime objects for easier date manipulation and comparison.
/* TODO */
/* Add additional examples to this convert method */
/* Including series, and numpy methods */


## 5.3 Removing Duplicates

### Overview

Duplicate records can inflate metrics and skew results. Removing duplicates ensures that each record is unique, which improves the reliability of analyses. Pandas provides the `drop_duplicates()` method to identify and remove duplicate rows.

### Key Method

- `drop_duplicates()`: Removes duplicate rows based on one or more columns.

### Why Remove Duplicates?

- Prevents redundant information in analysis.
- Improves data quality and storage efficiency.
- Ensures unique data for accurate insights.

### Example: Using `drop_duplicates()`

```python
import pandas as pd

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

**Explanation:**

`drop_duplicates()` removes rows where the entire record is a duplicate of another.
`drop_duplicates(subset='Name')` removes rows where the `Name` column is duplicated, keeping only the first occurrence of each name.

## 5.4 Handling outliers
### Overview
Outliers can also inflate metrics and skew results, by providing data that is clearly inacurate. Removing outliers ensures that our records don't have clear errors, which improves the reliability of analyses.
While duplicates are easy to remove outliers are more complex. You need to confirm that the data you are looking at is an outlier, and decide what you want to replace it with.   
### Key Method

Unlike other subjects in this chapter there are 2 steps to removing outliers. First we must determine what data is an outlier, and second we must remove it from the data frame.

To determine outliers we can use 

### Why handle outliers

Sometimes you will recieve data that is clearly and obviously incorrect. In those cases it can be wise to remove the data so that it will not interact with the data that is accurate. Consider if you are determining the age of everyone in a county. In your data set some people never had a death recorded in your county, leaving you with some people who are marked as being over 300 years old. In that case the only reasonable thing to do is to remove the outling data. 


### Example

**Check for Understanding**

Which method removes rows with missing values?

A) `fillna()`
B) `dropna()`
C) `remove_missing()`
D) `replace_na()`

**Answer:** B

<details>
<summary>Answer</summary>
Answer: B
</details>

How do you convert a column of strings to integers?

A) `pd.to_int(column)`
B) `df['column'].convert(int)`
C) `df['column'].astype(int)`
D) `df['column'].to_int()`

<details>

<summary>Answer</summary>

**Answer**: C

</details>


Which method is used to remove duplicate rows in Pandas?

A) `remove_duplicates()`
B) `drop_duplicates()`
C) `find_duplicates()`
D) `remove_redundant()`

<details>

<summary>Answer</summary>

**Answer**: B

</details>

**Summary**

In this lesson, you’ve learned:

* How to handle missing data using `dropna()` and `fillna()`.
* How to transform data by converting data types, reformatting dates, **performing feature engineering**, and **discretizing continuous variables**.
* How to identify and remove duplicate records with `drop_duplicates()`.

By applying these techniques, you can clean and validate your datasets for accurate and effective analysis. For further exploration, refer to the Pandas Documentation and Python's official documentation.
