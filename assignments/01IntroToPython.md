# Lesson 1 Assignment: Intro to Python  
**Objective:** Data Conversion, User Input, Error Handling, Functions, and Additional Concepts

---

**Instructions:**  
- Start by creating a `.py` file on your local machine. We recommend creating a `PythonClass` folder on your Desktop for organizing your work.
- You may use Visual Studio Code, a command terminal, or Jupyter Notebooks for your development environment.
- For Jupyter Notebooks, follow this resource on how to get started in VS Code: [Getting Started with Jupyter in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
- Complete the following tasks by writing code and modifying it where required. Ensure to add comments where needed to explain your thought process.

---

### Task 1: Data Type Conversion

1. **Create a variable `num_str`**  
    - Create a variable called `num_str` and assign it a string value representing a number (e.g., `"25"`).

2. **String to Integer Conversion**  
    - Convert the variable `num_str` (a string representing a number) to an integer.  
    - Perform an arithmetic operation using the converted integer and another variable `age`.  
    - Print the result.

3. **Float to String Conversion**  
    - Create a variable `height` (a float) and convert it to a string.  
    - Concatenate the float value as a string with another string (e.g., `" meters"`).  
    - Print the result.

4. **Integer to Float Conversion**  
    - Create a variable `age` (an integer) and convert it to a float.  
    - Print the result.

---

### Task 2: Simple Calculator

1. **User Input**  
    - Ask the user to input two numbers (`num1` and `num2`).

2. **Arithmetic Operations**  
    - Perform the following operations using the two inputted numbers:  
      - Addition  
      - Subtraction  
      - Multiplication  
      - Division  
    - Handle any errors if the user attempts to divide by zero, and display an error message.

3. **Print Results**  
    - Print the results of the arithmetic operations.

---

### Task 3: Grading System

1. **User Input for Score**  
    - Ask the user to enter their score (as a float).

2. **Determine Grade**  
    - Assign a grade based on the score:  
        - A: 90 and above  
        - B: 80-89  
        - C: 70-79  
        - D: 60-69  
        - F: below 60  

3. **Print Grade**  
    - Print the grade the user received based on their input.

4. **Allow the user to enter multiple scores**  
    - Store them in a list, calculate and display the average score, and the corresponding grade.

---

### Task 4: Function to Calculate Average

1. **Create a Function**  
    - Create a function called `calculate_average` that takes a list of numbers as an argument.  

2. **Calculate and Return Average**  
    - The function should calculate and return the average of the numbers in the list.  
    - If the list is empty, return 0.

3. **Test the Function**  
    - Test the function with the list `[1, 2, 3, 4, 5]` and print the result.

4. **Input validation**  
    - Ensure the list contains only numeric values before calculating the average. If the list contains invalid data, print an appropriate error message.

---

### Task 5: Calculator with Error Handling

1. **Create a Function for Division**  
    - Create a function called `divide_numbers` that takes two arguments (`num1` and `num2`).

2. **Implement Error Handling**  
    - Use a try-except block to handle division by zero. Return an appropriate error message if division by zero occurs.

3. **Test the Function**  
    - Ask the user to input two numbers, call the `divide_numbers` function, and print the result.

4. **Extend error handling**  
    - Handle other errors, such as when the user enters a non-numeric value. Implement appropriate error handling for these scenarios.

---

### Task 6: Working with Lists and Loops

1. **Create a List**  
    - Create a list of 5 integers. Print the list.

2. **Loop Through the List**  
    - Use a loop to print each number in the list, followed by its square. Example output:  
      `1: 1`, `2: 4`, `3: 9`, `4: 16`, `5: 25`

3. **Calculate and print the sum of the numbers in the list.**

---

### Task 7: File Handling

1. **Create a File**  
    - Create a new file called `numbers.txt` and write a series of numbers to it (one number per line).

2. **Read from the File**  
    - Read the contents of the file, convert the numbers back to integers, and store them in a list.

3. **Process the List**  
    - Calculate and print the sum of the numbers in the list.

---

### Submission:
- Submit the Python file (`.py`), Jupyter Notebook (`.ipynb`).
- Make sure your code is well-commented, neatly organized, and that all required tasks are completed.

---

