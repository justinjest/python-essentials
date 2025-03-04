# Lesson 3 — Intro to Data Engineering

## Lesson Overview

**Learning objective:** Students will learn to load, preview, and inspect datasets in Pandas by reading data from common formats and summarizing data structure to facilitate efficient data analysis.

Topics:

  * Introduction to Pandas: Creating and manipulating DataFrames.
  * Loading Data: Reading data from CSV, JSON, and dictionaries.
  * Data Inspection: Using head(), tail(), info() to inspect datasets.

## 3.1 Intro to Pandas

**Pandas** is a very powerful, open-source library for data analysis and manipulation in Python. It's widely used for handling and analyzing data structures, particularly in tabular format. With Pandas, you can work easily with structured data, perform data cleaning, and conduct complex transformations.  You can read more about pandas [here](https://pandas.pydata.org/docs/index.html).

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

### The numpy library ###

The numpy library provides highly optimized datatypes and numerical operations for python.  It is written in c and compiled to binary code which is linked with python.  Numerical computation in python using numpy are competitive with compiled languages like c++ and much faster than native python.  The pandas library is built on top of numpy and numpy numbers are often used with pandas.  You can read more about numpy [here](https://numpy.org/).

### Key Data Structures

1. **Series**: A one-dimensional array-like structure, similar to a list or array, but with added features such as **customizable indexes**. Each element in a Series is associated with a label (the index), allowing for more intuitive data manipulation and access.
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

A Series is a one dimensional data structure.  The column on the left is the index.  The column on the right is the data.

#### Key Features of a Series:
1. **Customizable Indexes**:
   - Unlike standard lists or arrays, a Series can have user-defined labels for its indices, making it easier to differentiate and access data.
   - For example:
     ```python
     import pandas as pd # The import only needs to be done once per interactive session
     data = pd.Series([10, 20, 30], index=["a", "b", "c"])
     print(data)
     # Output:
     # a    10
     # b    20
     # c    30
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

#### Loading data from numpy objects
In addition to initialization from python Lists and Dictionaries demonstrated in the examples above, Pandas can be initialized from numpy objects.

```python
import numpy as np # load the numpy library
# Create a Pandas DataFrame using NumPy arrays
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

print(df)

```

#### the DataFrame index
DataFrames include an index which can be thought of as a row number.  It can be useful for operations such as indexing, data alignment and subsetting.  For some of the operations we will discuss, we add an optional parameter to ignore the index since there is additional complexity involved in setting it up correctly.  For example, the index would need to be reset when combining two DataFrames.

#### Example: Differentiating a Series from a List
```python
# List Example
my_list = [10, 20, 30]
print(my_list[1])  # Access by position
# Output: 20

# Series Example
my_series = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(my_series["b"])  # Access by index label
# Output: 20
```

### Common Operations in Pandas

#### Reading Data
Pandas makes it easy to read data from files. For instance, to read data from a CSV file: 

```python
# Read data from a CSV file
df = pd.read_csv('data.csv')
```

#### Combining two DataFrames
The `concat` method can be used to combine two DataFrames.

```python
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
})

more_data = pd.DataFrame({
  'Name': ['Fred', 'Barney'],
  'Age': [57, 55],
  'City': ['Bedrock', 'Bedrock']
})

combined_df = pd.concat([data, more_data], ignore_index=True)
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
Handling missing data and cleaning data is essential in data analysis.  These are some examples of the data cleaning methods which are available.

#### Converting Columns to Numeric

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Height": ["5.5", "unknown", "5.9"],  # "unknown" is not numeric
    "Weight": ["60", "70", "NaN"]        # "NaN" is a missing placeholder
}
df = pd.DataFrame(data)

print("Before conversion:")
print(df)

# Replace placeholders with NaN and convert to numeric
df["Height"] = df["Height"].replace("unknown", pd.NA)
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")
df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")

print("\nAfter conversion to numeric:")
print(df)

 
```

#### Handling Missing Values with `fillna()`

```python
import pandas as pd
import numpy as np

data = {
    "Person": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "Score": [10, np.nan, 20, None, 25],
    "City": ["New York", "Chicago", None, "Boston", "NaN"]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Strategy 1: Fill numeric missing values with a fixed number
df["Score_filled_fixed"] = df["Score"].fillna(0)

# Strategy 2: Fill numeric missing values with the column mean
mean_score = df["Score"].mean()  # ignoring NaNs
df["Score_filled_mean"] = df["Score"].fillna(mean_score)

# Strategy 3: Fill textual missing values with "Unknown"
df["City_filled"] = df["City"].replace("NaN", pd.NA).fillna("Unknown")

print("\nDataFrame after fillna strategies:")
print(df)


```

#### Forward fill and backward fill

Handle missing data in a time series or sequential data scenario.

```python
import pandas as pd
import numpy as np

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sales": [100, np.nan, 150, np.nan, 200]
}
df = pd.DataFrame(data)

print("Original Sales Data:")
print(df)

# Forward fill (propagate last valid observation forward)
df_ffill = df.copy()
df_ffill["Sales"] = df_ffill["Sales"].fillna(method="ffill")

# Backward fill (use next valid observation to fill gaps)
df_bfill = df.copy()
df_bfill["Sales"] = df_bfill["Sales"].fillna(method="bfill")

print("\nForward Fill Result:")
print(df_ffill)

print("\nBackward Fill Result:")
print(df_bfill)


```

#### Text Standardization (strip, upper, lower)

```python
import pandas as pd

data = {
    "Department": [" SALES ", "   HR", "FinanCe  ", "Sales", "MARKETING "],
    "Location": [" New York ", " Boston", "Chicago   ", "  Boston ", "LOS ANGELES"]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Strip whitespace
df["Department"] = df["Department"].str.strip()
df["Location"] = df["Location"].str.strip()

# Convert columns to uppercase
df["Department_upper"] = df["Department"].str.upper()
df["Location_upper"] = df["Location"].str.upper()

# Or lowercase, if you prefer
df["Department_lower"] = df["Department"].str.lower()

print("\nAfter text standardization:")
print(df)


```

### Saving DataFrames to CSV Files

Pandas makes it easy to save DataFrames as CSV files, which is useful for sharing, storing, or exporting data for later use. You can use the to_csv() method to save your DataFrame to a CSV file
```python
DataFrame.to_csv(filepath, sep=',', index=True, header=True, encoding=None)
```
```filepath```: The name or path of the CSV file to save (e.g., ```"output.csv"```)   
```sep```: The delimiter to use (default is a comma ```,```).   
```index```: Whether to include the index as a column in the file (default is ```True```).   
```header```: Whether to include column names as the first row (default is ```True```).


### Save a DataFrame to a CSV File
```python
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [26, 31, 36],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Salary': [70000, 80000, 90000]
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("employees.csv", index=False)

print("DataFrame saved to employees.csv")
```
Output File (employees.csv):

```sql
Name,Age,City,Salary
Alice,26,New York,70000
Bob,31,Los Angeles,80000
Charlie,36,Chicago,90000

```
### 3.1 Videos: Installing and Using Pandas

In these two videos, we'll walk through installing and using Pandas in Python. This is an important step! If you're still feeling confused, contact a 1:1 mentor to walk through Pandas.

**[Video: What is Pandas? Why and How to Use in Python](https://youtu.be/dcqPhpY7tWk?feature=shared).**

*Note: The above video demonstrates using Pandas with Jupytr notebook. If you would like a look at using Pandas in VS Code, take time to look at the video below as well.*

**[Video: Installing Pandas in VSCode](https://youtu.be/4WZK0eovQIA?feature=shared).**

### 3.1 Check for Understanding

1. Which data structure is used for storing a two-dimensional table in Pandas?
  * A) List
  * B) Array
  * C) DataFrame
  * D) Series

<details>

<summary>Answer</summary>
1. C) DataFrame
</details>


2. How can you select rows in a DataFrame where a specific column value is greater than 10?
  * A) `df.loc[df['column'] > 10]`
  * B) `df.loc[df['column'] < 10]`
  * C) `df['column'] > 10`
  * D) `df.loc(column > 10)`
  
<details>

<summary>Answer</summary>
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

Here, `df.head()` will display the first five rows of the DataFrame by default. You can also customize `pd.read_csv()` with various parameters:

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

The JSON structure should be either a list of dictionaries (each representing a row) or a dictionary of lists (each representing a column). Here’s two examples of JSON data that can be read into a DataFrame:

```json
[
    {"Name": "Alice", "Age": 24, "City": "New York"},
    {"Name": "Bob", "Age": 27, "City": "San Francisco"},
    {"Name": "Charlie", "Age": 22, "City": "Chicago"}
]
```

The same DataFrame can be read using this JSON structure.  It's a bit simpler since it doesn't repeat the column names.

```json
{ "Name": ["Alice", "Bob", "Charlie"],
  "Age": [25, 30, 35],
  "City": ["New York", "Los Angeles", "Chicago"]
}
```

For complex JSON structures, you may need to specify additional parameters, or preprocess the JSON data before loading.



### Using the `sep` Parameter in Pandas

In **Pandas**, the `sep` parameter is commonly used when reading or writing CSV (or similar) files. It specifies the **delimiter** (separator) used in the file to distinguish between columns.


### Common Methods with `sep`

1. **`pd.read_csv()`**: Reads a file and uses the `sep` parameter to define how columns are separated.

2. **`DataFrame.to_csv()`**: Exports a DataFrame and uses `sep` to specify the delimiter in the output file.


### Example 1: Reading a CSV File with a Custom Separator

Some CSV files may use delimiters other than a comma, such as tabs (`\t`) or pipes (`|`).

```python
import pandas as pd

# Read a CSV file with pipe as the separator
data = pd.read_csv("data.csv", sep="|")
print(data.head())
```

If the file contains:

```sql
Name|Age|City
Alice|30|New York
Bob|25|Los Angeles
```

The output will be:

```markdown
    Name  Age         City
0  Alice   30     New York
1    Bob   25  Los Angeles
```

### Example 2: Writing a CSV File with a Custom Separator

You can export a DataFrame using a custom delimiter instead of the default comma.

```python
# Create a sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [30, 25],
    "City": ["New York", "Los Angeles"]
})

# Save the DataFrame to a CSV file with a tab as the separator
df.to_csv("output.tsv", sep="\t", index=False)
```

The output file `output.tsv` will look like this:

```sql
Name	Age	City
Alice	30	New York
Bob	25	Los Angeles
```

#### Why Use `sep`?

* **Flexibility:** Handle files with different delimiters (e.g., tabs, pipes, semicolons).
* **Compatibility:** Work with non-standard or region-specific CSV formats.

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

### 3.2 Check for Understanding

1. Which function is used to load data from a JSON file into a DataFrame?

  * A) pd.read_csv()
  * B) pd.read_json()
  * C) pd.DataFrame()
  * D) pd.read_dict()
<details>

<summary>Answer</summary>
1. B) `pd.read_json()`
</details>

2. If your CSV file uses semicolons (;) instead of commas, which parameter can you use to specify this in pd.read_csv()?

  * A) separator
  * B) delimiter
  * C) sep
  * D) Both b and c

<details>

<summary>Answer</summary>

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
| `tail()`       | Displays the last five rows of the DataFrame  | 
| `info()` | Summarizes the DataFrame, including data types, null counts, and memory usage  | 

### 3.3 Check for Understanding

1. What is the default number of rows displayed when using `df.head()`?

     * A) 3
     * B) 5
     * C) 7
     * D) 10
 <details>

<summary>Answer</summary> 
1. B) 5
</details>
  
2. Which method provides information about column data types and memory usage?

     * A) `head()`
     * B) `tail()`
     * C) `summary()`
     * D) `info()`

<details>

<summary>Answer</summary> 

2. D) `info()`

</details>

---
This content was written by Janet Zulu, Reid Russom, and CTD volunteers—with special thanks to the brain trust of John McGarvey, Rebecca Callari-Kaczmarczyk, Tom Arns, and Josh Sternfeld. To submit feedback, please fill out the **[CTD Curriculum Feedback Form](https://forms.gle/RZq5mav7wotFxyie6)**.
