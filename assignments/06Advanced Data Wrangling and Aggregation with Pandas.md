# Advanced Data Cleaning and Validation Assignment

This assignment is to be created in a Kaggle notebook, as you did for Assignments 4 and 5.  This time, create a notebook called CTD_Assignment_6 for code as described below.

Complete the tasks below to demonstrate your understanding of data cleaning and validation techniques. Submit your code and outputs for each task.

---

## Task 1: Clean Address Data
1. Create a list called `text_data` containing the following address strings:
   - `" 123 Main St"`
   - `"456 Elm St."`
   - `"789 Pine Avenue"`
2. Write a script using the `re` module to:
   - Remove any extra spaces between words.
   - Strip leading and trailing spaces.
3. Store the cleaned addresses in a new list called `cleaned_data`.
4. Print the cleaned addresses.

---

## Task 2: Handle Outliers in a DataFrame
1. Create a dictionary named `data_with_outliers` with two columns:
   - `Name`: A list of names (`['Alice', 'Bob', 'Charlie']`).
   - `Age`: A list of ages (`[25, 130, 35]`).
2. Convert the dictionary into a DataFrame called `df_outliers`.
3. Identify and replace outliers in the `Age` column:
   - Define outliers as ages greater than 100.
   - Replace these outliers with the median value of the `Age` column.
4. Print the updated DataFrame.

---

## Task 3: Impute Missing Values
1. Create a dictionary with the following data:
   - `Name`: A list of names (`['Alice', 'Bob', 'Charlie']`).
   - `Age`: A list of ages with a missing value (`[25, None, 35]`).
2. Convert the dictionary into a DataFrame called `df_nan`.
3. Calculate the median value of the `Age` column.
4. Fill the missing value in the `Age` column with the calculated median.
5. Print the updated DataFrame.

---

### **Submit the Notebook for Your Assignment**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Get a Sharing Link for Your Assignment**  
- On the upper right of the Kaggle page, click on Save Version and save, accepting all defaults.  You can just do a quick save.
- On the upper right, click on Share.  Choose Public, make sure that Allow Comments is on, and copy the public URL to your clipboard.

#### **2️⃣ Submit Your Kaggle Link**  
- Paste the URL into the **assignment submission form**.  

---
