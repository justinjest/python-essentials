# Advanced Data Cleaning and Validation Assignment

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

### Submit Your Assignment on GitHub**  

📌 **Follow these steps to submit your work:**  

#### **1️⃣ Upload Your Assignment**  
- Go to your `python-essentials` GitHub repository.
- Click the **Add file** dropdown and select **Create new file**.
- Create a folder for this lesson by typing the lesson name followed by a `/` (i.e., `lesson-05/`)
- Name the file by typing the file name. (i.e., `lesson-05/assignment.py` or `lesson-05/assignment.ipynb` for a Jupyter Notebook).  
- Paste your code into the file OR click **Upload files** and add your `.py` or `.ipynb` file.  
- Click **Commit new file** to save your work.  

#### **3️⃣ Submit Your GitHub Link**  
- Open your repository and navigate to the `lesson-05` folder.  
- Copy the URL of the folder (e.g., `https://github.com/your-username/python-class-your-name/tree/main/lesson-05`).  
- Paste the URL into the **assignment submission form**.  

---

## **✅ Submission Checklist**  
Before submitting, make sure:  
- [ ] Your repository follows the format `python-class-your-name`.  
- [ ] Your assignment is inside a `lesson-05` folder.  
- [ ] You've uploaded your `.py` or `.ipynb` file.  
- [ ] You’ve copied and submitted the correct GitHub folder URL.
- [ ] Ensure each task is commented appropriately to explain your code.

---
