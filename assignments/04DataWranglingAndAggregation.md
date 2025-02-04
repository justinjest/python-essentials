## Lesson 4 Assignment — Data Wrangling and Manipulation
### Advanced Data Wrangling and Aggregation with Pandas

### **Objective:**
The purpose of this assignment is to deepen your understanding of data wrangling and aggregation using the Pandas library in Python. You will work with sample DataFrames to perform various operations such as filtering, handling missing values, merging, sorting, transforming, and creating pivot tables.

### **Setup**

The assignments up to this one have required you to create `.py` files and to submit them by creating pull requests for your python_homework repository.  For this assignment, you create a Jupyter notebook file.  Jupyter notebooks are a way to do data presentation and analysis, using Python code.  A notebook is comprised of a sequence of cells, which come in two kinds: Markdown cells, for putting in the text you want to show, and code cells, where you put your Python code.

With a little setup, you can create Jupyter notebooks in VSCode, and submit them to GitHub.  However, GitHub is not a friendly environment for collaboration on notebooks.  Your reviewer wants to see the notebooks, to run them, and to give you comments in context.  For that purpose, we use [https://kaggle.com].  That site also has an interesting collections of data sets you can use for practice in data analysis and presentation.  Connect to the site now and register, so that you have an account.

### **Tasks:**

### **Task 1: Data Selection**
1. On the Kaggle site, click on the plus button in the upper left, and create a notebook called CTD_Assignment_4.  It comes up with a code cell already present.  Leave that one alone, and click on the plus code button to add another cell.  You add the code for this assignment to the cell.  As you complete each of the following tasks, run the cell to make sure your code works.  You run the cell by clicking on the arrow at the top left of the cell.
1. **Create two DataFrames `df1` and `df2` using the provided sample data(feel free to change the values):**
   - `df1` contains names, ages, and salaries of five employees.
   - `df2` contains names, ages, and salaries of five other employees.
   - Display both DataFrames.
   
```
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 30],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}
```

```
data2 = {
    'Name': ['Frank', 'Grace', 'Helen', 'Ian', 'Jack'],
    'Age': [28, 33, 35, 29, 40],
    'Salary': [52000, 58000, 72000, 61000, 85000]
}

```
Print the resulting dataframes.
2. **Perform the following selection operations on `df1`:**
   - Select the 'Name' column, and print the result.
   - Select both 'Name' and 'Salary' columns, and print the result.
   - Slice the first three rows using integer-based indexing (`iloc`).

### **Task 2: Data Aggregation**
1. **Group `df1` by 'Age' and aggregate the 'Salary' column:**
   - Calculate the mean, sum, and count of the salary for each age group.
   - Display the aggregated results.

### **Task 3: Merging and Joining DataFrames**
1. **Merge `df1` and `df2` on the 'Name' column:**
   - Use an outer join to combine the two DataFrames and handle any missing data.
   - Use the suffixes `_df1` and `_df2` to differentiate columns from each DataFrame.

2. **Join `df1` and `df2` using the `join()` method:**
   - Set 'Name' as the index before joining the DataFrames.
   - Display the joined DataFrame with outer join logic.

### **Task 4: Filtering Rows Based on Conditions**
1. **Filter rows in `df1` where 'Age' is greater than 30:**
   - Display the filtered rows.

### **Task 5: Handling Missing Values**
1. **Handle missing values in the merged DataFrame:**
   - Replace any `NaN` values with 0.
   - Display the updated DataFrame.

### **Task 6: Sorting Data**
1. **Sort `df1` by the 'Salary' column in descending order:**
   - Display the sorted DataFrame.

### **Task 7: Renaming Columns**
1. **Rename columns in `df1`:**
   - Rename 'Age' to 'Employee Age' and 'Salary' to 'Employee Salary'.
   - Display the DataFrame with the renamed columns.

### **Task 8: Creating a Pivot Table**
1. **Create a pivot table for `df1`:**
   - Use 'Age' as the index and 'Salary' as the value.
   - Aggregate the salary using the mean function.
   - Display the pivot table.

**Hint:** Use the `pivot_table()` function in Pandas, setting 'Age' as the index and 'Salary' as the values. Aggregate the salary using the mean function.

### **Task 9: Data Transformation**
1. **Apply a transformation to the 'Salary' column in `df1`:**
   - Increase the salary by 10% for each employee.
   - Display the updated DataFrame.

### **Task 10: Concatenating DataFrames**
1. **Concatenate `df1` and `df2` along rows:**
   - Reset the index before concatenating and display the concatenated DataFrame.

### **Task 11: Cross Tabulation**
1. **Create a cross-tabulation of ages in the concatenated DataFrame:**
   - Display the frequency of each age for different names.

### Submit Your Assignment on GitHub**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Get a Sharing Link for Your Assignment**  
- On the upper right of the Kaggle page, click on Save Version and save, accepting all defaults.  You can just do a quick save.
- On the upper right, click on Share.  Choose Public, make sure that Allow Comments is on, and copy 

#### **2️⃣ Submit Your Kaggle Link**  
- Paste the URL into the **assignment submission form**.  

---
