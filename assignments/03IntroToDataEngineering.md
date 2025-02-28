## Lesson 3 Assignment — Intro to Data Engineering
### Data Analysis and Manipulation with Pandas

### **Objective:**
In this assignment, you will explore the basic functionalities of the Pandas library in Python, including creating, manipulating, inspecting, and analyzing data using various DataFrame methods. The goal is to understand how to handle data efficiently and perform essential operations to inspect and analyze datasets.

### **Step 1: Complete the Coding Tasks**  

Homework for this assignment is created within your `python_homework` folder.  Create an `assignment3` branch and checnge to the `assignment3` folder.  Write your code in `assignment3.py`.  As with the previous lessons, you will run unit tests on the assignment `pytest -v -x assignment3-test.py`.

---

### **Tasks:**

### **Task 1: Introduction to Pandas - Creating and Manipulating DataFrames**
1. **Create a DataFrame from a dictionary:**
   - Use a dictionary containing the following data:
     - `Name`: ['Alice', 'Bob', 'Charlie']
     - `Age`: [25, 30, 35]
     - `City`: ['New York', 'Los Angeles', 'Chicago']
   - Convert the dictionary into a DataFrame using Pandas.
   - Print the DataFrame to verify its creation.
   - save the DataFrame in a variable called `task1_data_frame`

2. **Add a new column:**
   - Make a copy of the dataFrame you created named `task1_with_salary` (use the `copy()` method)
   - Add a column called `Salary` with values `[70000, 80000, 90000]`.
   - Print the new DataFrame

3. **Modify an existing column:**
   - Make a copy of `task1_with_salary` in a variable named `task1_older`
   - Increment the `Age` column by 1 for each entry.
   - Print the modified DataFrame to verify the changes.

4. **Save the DataFrame as a CSV file:**
   - Save the `task1_older` DataFrame to a file named `employees.csv` using ```to_csv()```.
     

### **Task 2: Loading Data from CSV, JSON, and Dictionaries**
1. **Read data from a CSV file:**
   - Create a sample CSV file using the DataFrame from Task 1.
   - Load the CSV file into a new DataFrame and print it.

2. **Read data from a JSON file:**
   - Create a JSON file (additional_employees.json) with the following data:
     
```

  {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
  {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}

```
   - Load this JSON file into a new DataFrame using pd.read_json().
   - Print the DataFrame to verify it loaded correctly


3. **Combine DataFrames:**
   - Append the data from the JSON file to the DataFrame Loaded from the CSV file.
   - Print the combined Dataframe

### **Task 3: Data Inspection - Using Head, Tail, and Info Methods**
1. **Use the `head()` method:**
   - Print the first 5 rows of the original dictionary DataFrame using the `head()` method.

2. **Use the `tail()` method:**
   - Print the last 2 rows of the original dictionary DataFrame using the `tail(2)` method.

3. **Use the `info()` method:**
   - Print a concise summary of the DataFrame using the `info()` method to understand the data types and non-null counts.

### **Task 4: Additional Data Inspection and Analysis**
1. **Determine the shape of the DataFrame:**
   - Use the `shape` attribute to print the number of rows and columns in the original DataFrame.

2. **Use the `describe()` method:**
   - Print a statistical summary of the numeric columns in the DataFrame, including count, mean, standard deviation, min, max, and quartiles.

3. **Calculate the correlation matrix:**
   - Use the `corr()` method to print the correlation matrix of the numeric columns, indicating how the columns are related to each other.

---

### **Step 2: Submit Your Assignment on GitHub**  

**Follow these steps to submit your work:**  

#### **1️⃣ Add, Commit, and Push Your Changes**  
- Within your python_homework folder, do a git add and a git commit for the files you have created, so that they are added to the `assignment3` branch.
- Push that branch to GitHub. 

#### **2️⃣ Create a Pull Request**  
- Log on to your GitHub account.
- Open your `python_homework` repository.
- Select your `assignment3` branch.  It should be one or several commits ahead of your main branch.
- Create a pull request.

#### **3️⃣ Submit Your GitHub Link**  
- Your browser now has the link to your pull request.  Copy that link. 
- Paste the URL into the **assignment submission form**.  

---
