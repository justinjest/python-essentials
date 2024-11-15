# Lesson 3 — Intro to Data Engineering

## Lesson Overview

**Learning objective:** Students will learn to load, preview, and inspect datasets in Pandas by reading data from common formats and summarizing data structure to facilitate efficient data analysis.

Topics:

  * Introduction to Pandas: Creating and manipulating DataFrames.
  * Loading Data: Reading data from CSV, JSON, and dictionaries.
  * Data Inspection: Using head(), tail(), info() to inspect datasets.

## 3.1 Intro to Pandas

**Pandas** is a powerful, open-source library for data analysis and manipulation in Python. It's widely used for handling and analyzing data structures, particularly in tabular format. With Pandas, you can work easily with structured data, perform data cleaning, and conduct complex transformations.

### Why Use Pandas? 
Pandas provides data structures like **DataFrames** and **Series** that make data manipulation in Python simpler and faster. It's well-suited for tasks that involve:

  * Loading data from different file formats (CSV, Excel, SQL, etc.)
  * Cleaning and transforming messy data
  * Summarizing data for analysis
  * Visualizing data with integration to other libraries like Matplotlib and Seaborn

### Getting Started with Pandas
To get started, install Pandas using pip: 

```bash
pip install pandas
```

Then, you can import it in your Python code: 

```python
import pandas as pd
```

### Key Data Structures

1. **Series**: A one-dimensional array, similar to a list or array, but with added features like an index.
2. **Data Frame:** A two-dimensional table where each column can hold different types of data. This is the most commonly used data structure in Pandas.

#### Example: Creating a Series
Run the following code in Python:

```python
# Creating a simple Series
import pandas as pd

data = [1, 3, 5, 7, 9]
s = pd.Series(data, name="numbers")
print(s)
```

The output should be: 

```yaml
0    1
1    3
2    5
3    7
4    9
Name: numbers, dtype: int64
```

#### Example: Creating a DataFrame
DataFrames are like tables in a database or spreadsheet. To create a DataFrame from a dictionary, run the following code in Python: 

```python
# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
```

The output should be: 

```markdown
      Name  Age           City
0    Alice   24       New York
1      Bob   27  San Francisco
2  Charlie   22        Chicago
```

### Common Operations in Pandas

#### Reading Data
Pandas makes it easy to read data from files. For instance, to read data from a CSV file: 

```python
# Read data from a CSV file
df = pd.read_csv('data.csv')
```

#### Data Selection
You can select rows and columns in various ways. 

```python
# Select a single column
print(df['Age'])

# Select multiple columns
print(df[['Name', 'City']])

# Select rows by index position
print(df.iloc[1])  # Select the second row

# Select rows by condition
print(df[df['Age'] > 23])
```

### Data Aggregation
Pandas also allows for powerful aggregations, such as finding the mean or sum of a column. 

```python
# Find the average age
print(df['Age'].mean())

# Count the number of unique cities
print(df['City'].nunique())
```

### Data Cleaning
Handling missing data and cleaning data is essential in data analysis.

```python
# Drop rows with missing values
df = df.dropna()

# Fill missing values with a default value
df = df.fillna(0)
```

### 3.1 Video: Installing and Using Pandas

In this video, one of our mentors will demonstrate installing and using Pandas in Python. This is an important step! If you're still feeling confused, contact a 1:1 mentor to walk through Pandas.

View the video here: [LINK TBD]

### 3.1 Check for Understanding

1. Which data structure is used for storing a two-dimensional table in Pandas?
  * A) List
  * B) Array
  * C) DataFrame
  * D) Series

2. How can you select rows in a DataFrame where a specific column value is greater than 10?
  * A) `df.loc[df['column'] > 10]`
  * B) `df.loc[df['column'] < 10]`
  * C) `df['column'] > 10`
  * D) `df.loc(column > 10)`
  
<details>

<summary>Answer</summary>

**Answers**:

1. C) DataFrame
2. A) `df.loc[df['column'] > 10]`

</details>

Great work! With these basics, you can now start using Pandas for various data manipulation and analysis tasks.

## 3.2 Loading Data in Pandas

Pandas provides convenient methods for loading data from various sources, such as CSV and JSON files, as well as Python dictionaries. This makes it easy to get your data into a format where you can start analyzing it.

### Reading Data from a CSV File

As you recall from Lesson 2, **CSV** (Comma-Separated Values) is one of the most common data formats, especially for tabular data. Pandas makes it simple to read and manipulate CSV files.

#### Example: Reading a CSV File

To load a CSV file, use `pd.read_csv()`.

```python
import pandas as pd

# Load the data from a CSV file
df = pd.read_csv('data.csv')
print(df.head())
```

Here, `df.head()` will display the first five rows of the DataFrame. You can also customize `pd.read_csv()` with various parameters:

```python
# Loading a CSV file with custom parameters
df = pd.read_csv('data.csv', delimiter=';', header=0, index_col='ID')
```

In the above example,
  * `delimiter` defines a custom separator (e.g., `;`)
  * `header` indicates the row for column headers (defaults to the first row)
  * `index_col` sets a column to be used as the DataFrame index.

### Reading Data from a JSON File

**JSON** (JavaScript Object Notation) is another popular format, often used for data exchange on the web. Pandas can read JSON files directly into a DataFrame.

#### Example: Reading a JSON File

To load a JSON file, use `pd.read_json()`. Note that this function looks the same as the one we used for a CSV file, we've just replaced `csv` with `json`.

```python
# Load the data from a JSON file
df = pd.read_json('data.json')
print(df.head())
```

The JSON structure should be either a list of dictionaries (each representing a row) or a dictionary of lists (each representing a column). Here’s an example of JSON data that can be read into a DataFrame:

```json
[
    {"Name": "Alice", "Age": 24, "City": "New York"},
    {"Name": "Bob", "Age": 27, "City": "San Francisco"},
    {"Name": "Charlie", "Age": 22, "City": "Chicago"}
]
```

For complex JSON structures, you may need to specify additional parameters, or preprocess the JSON data before loading.

#### Loading Data from a Dictionary

Pandas also allows you to create DataFrames from Python dictionaries directly, which is useful when you already have data in a Python program.

#### Example: Loading Data from a Dictionary

If you have a dictionary where keys represent column names and values represent the data, you can use `pd.DataFrame()` to create a DataFrame.

```python
# Create a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)
print(df)
```

This will output: 

```markdown
      Name  Age           City
0    Alice   24       New York
1      Bob   27  San Francisco
2  Charlie   22        Chicago
```

### Summary of Methods

| Format     | Method           | Example                          |
|------------|-------------------|----------------------------------|
| CSV        | `pd.read_csv()`   | `df = pd.read_csv('data.csv')`   |
| JSON       | `pd.read_json()`  | `df = pd.read_json('data.json')` |
| Dictionary | `pd.DataFrame()`  | `df = pd.DataFrame(data)`        |

### 3.2 Video

[Video Topic TBD]. 

View the video here: [LINK TBD]

### 3.2 Check for Understanding

1. Which function is used to load data from a JSON file into a DataFrame?

  * A) pd.read_csv()
  * B) pd.read_json()
  * C) pd.DataFrame()
  * D) pd.read_dict()

2. If your CSV file uses semicolons (;) instead of commas, which parameter can you use to specify this in pd.read_csv()?

  * A) separator
  * B) delimiter
  * C) sep
  * D) Both b and c

<details>

<summary>Answer</summary>

**Answers**:


1. B) `pd.read_jason()`
2. D) Both B and C

</details>

With these functions, you’re equipped to load data from different formats into Pandas, ready for analysis!

## 3.3 Data Inspection

Once you've loaded data into a DataFrame, it’s essential to inspect it to understand its structure, spot any missing values, and identify the data types of each column. Pandas provides several convenient methods for quickly viewing and summarizing your dataset.

### Using `head()` and `tail()` to Preview Data

The `head()` and `tail()` methods allow you to preview the first or last few rows of your DataFrame. By default, they show 5 rows, but you can specify any number you want.

#### Example: Using `head()`

`head()` is typically used to get a quick look at the beginning of the dataset.

```python
import pandas as pd

# Load some sample data
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [24, 27, 22, 32, 29, 41],
    'City': ['New York', 'San Francisco', 'Chicago', 'Los Angeles', 'Houston', 'Seattle']
})

# Display the first 3 rows
print(df.head(3))
```

This will output: 

```markdown
      Name  Age           City
0    Alice   24       New York
1      Bob   27  San Francisco
2  Charlie   22        Chicago
```

#### Example: Using `tail()`

Similarly, `tail()` allows you to view the last few rows of the DataFrame.

```python
# Display the last 2 rows
print(df.tail(2))
```

This will output: 

```
    Name  Age     City
4    Eve   29   Houston
5  Frank   41   Seattle
```

### Using `info()` to Get a Summary of the DataFrame

The `info()` method provides a summary of the DataFrame, including: 
  * The number of entries (rows)
  * The data types of each column
  * The number of non-null (non-missing) values in each column
  * Memory usage of the DataFrame

#### Example: Using `info()`

```python
# Get a summary of the DataFrame
df.info()
```
This will output: 

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    6 non-null      object
 1   Age     6 non-null      int64 
 2   City    6 non-null      object
dtypes: int64(1), object(2)
memory usage: 272.0 bytes
```

From this output, you can see the column names, data types, number of non-null entries per column, and how much memory the DataFrame consumes. This summary is helpful for understanding the dataset's overall structure.

### Summary of Methods

| Format     | Description           | 
|------------|-------------------|
| `head()`        | Displays the first few rows of the DataFrame  | 
| `tail()`       | Displays the last few rows of the DataFrame  | 
| `info()` | Summarizes the DataFrame, including data types, null counts, and memory usage  | 

### 3.3 Video

[Video Topic TBD]. 

View the video here: [LINK TBD]

### 3.3 Check for Understanding

1. What is the default number of rows displayed when using `df.head()`?

     * A) 3
     * B) 5
     * C) 7
     * D) 10
  
2. Which method provides information about column data types and memory usage?

     * A) `head()`
     * B) `tail()`
     * C) `summary()`
     * D) `info()`

<details>

<summary>Answer</summary> 

**Answers**:

1. B) 5
2. D) `info()`

</details>

These methods will help you quickly inspect and understand your data before diving into further analysis!

---
This content was created by Janet Zulu, Reid Russom, and CTD volunteers. To submit feedback, please fill out the [CTD Curriculum Feedback Form (https://airtable.com/apphJi94mO4Uc7a3k/pagD3WQmswgXJvgx3/form).
