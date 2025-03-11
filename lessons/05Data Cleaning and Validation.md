
## Lesson 05 — Data Cleaning and Validation I

**Lesson Overview**

**Learning objective:** Students will learn techniques for handling missing data, transforming data types, and identifying and removing duplicate records to ensure data quality. This lesson will provide foundational skills necessary for cleaning raw data, ensuring it's ready for effective analysis.

### Topics

1. **What is Data Cleaning?**: An introduction to the concepts of data cleaning.
1. **Handling Missing Data**: Removing rows with `dropna()`, replacing values with `fillna()`.
2. **Data Transformation**: Converting data types, reformatting dates, **feature engineering**, **data discretization**.
3. **Removing Duplicates**: Identifying and removing duplicate records.
4. **Removing Outliers**: Identify and removing outlying records
---

## 5.1 What is Data Cleaning?

Data is often dirty.  Values may be missing, or duplicated, or incorrectly formatted, or have values that are not plausible or manageable by data analysis.  The following optional [video](https://www.youtube.com/watch?v=WpX2F2BS3Qc) expains the concepts.  The main idea is garbage-in, garbage-out.  Any analysis you do on data that is partly incorrect may be invalid.  Data cleaning involves the following procedures:

- Standardization.  For example, you want to represent dates and phone numbers in a standard way.  You also want to have consiten
- Addressing outliers.  These are values that appear improbable and were likely entered in error.
- Deduplication.
- Addressing missing values.
- Validation.

You will learn various technical approaches to each of these.

### Standardization

You can check, for example, that email addresses are of a valid format.  Suppose some are not.  You can either flag the rows for manual correction, or discard the rowss, or attempt to reformat the addresses to correct the problem, or derive the correct addresses from other information in the row or perhaps in a separate dataset.  For US phone numbers, you could check that each is a string of 10 numeric characters.

### Addressing Outliers

Sometimes outliers are easy to identify.  If a person's age is negative, or greater than 120, this is an outlier.  But in other cases, it might not be so clear.  For example, if you discarded outliers for daily rainfall in a region, you could end up discarding all flood events, which are important records that are needed for the analysis.

### Deduplication

Deduplication is pretty easy if the rows are exactly the same.  But, if one of the values in the row is a little bit different, it may not be as clear.  Perhaps you have access to a reliable key, such as a known phone number or email address.

### Addressing missing values

You can throw away the rows with missing information ... but other parts of the record may have valuable information.

You can substitute a plausible value ... but this distorts the data.  For example, if the data contains a person's net worth, you could substitute the mean value for that column, but actually most people don't have nearly the 'average' net worth.  You could substitute the median value instead, but again, most people have incomes that differ from the median by quite a bit.

Each automated change to clean the data involves a tradeoff.  You should always archive the original data, in case cleaning introduces distortions.

### Validation

This is a process to check that the cleaned data is in fact correct.  For example, for information about a person, you might want to ask the person if the stored information is correct.


## 5.1 Handling Missing Data

### Overview

Missing data is common in datasets and can significantly affect the outcome of analyses if not handled properly. In Pandas, there are methods to identify and handle missing data, either by removing rows or by filling in the missing values. Correctly managing missing data is crucial for ensuring accurate results.

### Key Methods

- `isnull()`: Find the rows where data is missing.
- `dropna()`: Removes rows or columns with missing data.
- `fillna()`: Replaces missing values with specified values.

### Why Handle Missing Data?

- Ensures accurate calculations and visualizations.
- Prevents runtime errors during analysis.
- Allows consistent dataset formatting.

### Example: Using `isnull()`, `dropna()` and `fillna()`

**For this and all examples below, you should run the code within the Python interactive shell of your python_homework VSCode terminal.**

```python
import pandas as pd

# Sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', None, 'David'],
        'Age': [24, 27, 22, None],
        'Score': [85, None, 88, 76]}
df = pd.DataFrame(data)

# Find rows with missing data
df_missing = df[df.isnull().any(axis=1)]
print(df_dropped)
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
In addition you can use the Series map() method to change items in a column.

```python
import pandas as pd

# Sample DataFrame

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)

# Convert 'Location' abbreviations into full names

df['Location'] = df['Location'].map({'LA': 'Los Angeles', 'NY': "New York"})
print(df)
```

The problem with the code above is that if the value in the 'Location' column is not either 'LA' or 'NY', it is converted to `NaN`.  Suppose you want to preserve the existing value in this case. You'd use the replace() method instead:

```python
df['Location'] = df['Location'].replace({'LA': 'Los Angeles', 'NY': "New York"})
```

Here is another case.  Suppose we have a list of people's phone numbers, but they are not in standard format.  We can attempt to clean this up in this way:

```python
import pandas as pd
data = {'Name': ['Tom', 'Dick', 'Harry', 'Mary'], 'Phone': [3212347890, '(212)555-8888', '752-9103','8659134568']}
df = pd.DataFrame(data)
df['Correct Phone'] = df['Phone'].astype(str)

def fix_phone(phone):
    if phone.isnumeric():
        out_string = phone
    else:
        out_string = ''
        for c in phone:
            if c in '0123456789':
                out_string += c
    if len(out_string) == 10:
        return out_string
    return None
    
df['Correct Phone'] = df['Correct Phone'].map(fix_phone)
print(df)
```
In the code above, the 'Phone' column is preserved, in case there is useful information, but the 'Correct Phone' column is created, with a best effort at reformatting the phone numbers.  Note that the logic did not fit in a lambda, so a function was declared to pass to map().

Finally we can use built in numpy functions in order to change all of the data in a data frame by following a function
```python

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
	'Age': [20, 22, 43]}

df = pd.DataFrame(data)

# Increase the age by 1 as a new year has passed
df['Age'] = df['Age'] += 1
print(df)
```


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
`pd.cut()` allows us to create bins for data and provide data discretization

---

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

---

## **5.4 Handling Outliers**

### **Overview**
Outliers are extreme values that deviate significantly from other observations and can bias statistical calculations.

### **Common Approach:**
- Replace outliers with statistical measures like the median.

### **Code Example:**

(You don't need to run this one, as the DataFrame is not provided.)

```python
# Replace outliers in 'Age' (e.g., Age > 100 or Age < 0)
df['Age'] = df['Age'].apply(lambda x: df['Age'].median() if x > 100 or x < 0 else x)

print("DataFrame after handling outliers:")
print(df)
```

### **Explanation:**
- Outliers in the `Age` column that are greater than 100 or less than 0 are replaced by the median value of the `Age` column.

---



### Example

**Check for Understanding**

Which method removes rows with missing values?

A) `fillna()`
B) `dropna()`
C) `remove_missing()`
D) `replace_na()`

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

* How to handle missing data using `isnull()`, `dropna()` and `fillna()`.
* How to transform data by converting data types, reformatting dates, and discretizing continuous variables.
* How to identify and remove duplicate records with `drop_duplicates()`.
* How to remove outliers using statistical methods.

By applying these techniques, you can clean and validate your datasets for accurate and effective analysis. For further exploration, refer to the Pandas Documentation and Python's official documentation.
