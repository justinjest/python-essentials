# Lesson 2 — Data Structures and File Handling

## 👀 Reminder: How to Follow This Content

* Start by reading the lesson's **learning objective** in the `Lesson Overview` section. Each weekly assignment will measure your skill related to the learning objective.
* Lessons are split into **subsections**, labeled like this: `1.1`, `1.2`, etc.
* Each subsection has a short **supplemental video** that will help you understand the content in that subsection.
* At the end of each subsection, you'll find a multiple-choice **"Check for Understanding"** question. Complete the question and review the material if your answer is not correct!
* After reading through the lesson content and correctly answering the "Check for Understanding" questions, complete the **Weekly Assignment**.

If you have questions at any point, ask a question in the `discussion` Slack channel or reach out to your mentor!

## Lesson Overview

Congrats, you've made it to Lesson 2! This week, we'll deepen our knowledge of core Python concepts, including dictionaries and lists. We'll also learn how to import **modules**, powerful tools that help your Python projects reach their full potential.
Additionally, we’ll learn how to work with the operating system (OS) and virtual environments for more efficient project management.

**Learning objective**: Students will explore various data structures, such as lists, tuples, dictionaries, and sets. They will learn how to read and write data to files and use external modules.  Additionally, they will be introduced to basic OS operations and using virtual environments.

Topics:

* Lists, Tuples, Dictionaries, and Sets: Creating, accessing, and modifying data structures.
* File Handling: Reading from and writing to text and CSV files.
* Introduction to Modules & packages: Importing and using Python libraries.
* Keyboard Input
* Working with the OS: Interacting with the file system and executing commands.
* Virtual Environments: Managing dependencies for Python projects.

## 2.1 Lists, Tuples, Dictionaries, and Sets

Before we talk about lists and tuples, we need to define two new words: "mutable" and "immutable."

Something that is **mutable** can be modified or changed after it is created. Something that is **immutable** cannot be modified or changed after it is created.

Imagine a piece of clay (mutable) versus a ceramic statue (immutable):

* Clay can be reshaped, squished, or molded into different forms after it's first created. You can add or remove parts easily.
* A ceramic statue, once it's fired in a kiln, cannot be changed without breaking it completely.

In Python programming, here's a concrete example using *mutable* lists and *immutable* tuples:

``` python
# Mutable example (list)
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')  # We can add a new item
fruits[0] = 'orange'  # We can change an existing item
print(fruits)  # Now ['orange', 'banana', 'cherry', 'date']

# Immutable example (tuple)
colors = ('red', 'green', 'blue')
# colors[0] = 'yellow'  # This would cause an error
# You cannot change the tuple after creation
```

### Lists

A **list** is a *mutable*, ordered collection of items. Lists allow duplicates and can hold items of different types, although typically you’ll find lists containing items of the same type. You can add, remove, or modify elements in a list, making them versatile for storing data that may change.

```python
fruits = ['apple', 'banana', 'cherry']  # Define a list
fruits.append('orange')  # Add an item
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

#### Key List Methods

* `append(item)`: Adds `item` to the end of the list.
* `remove(item)`: Removes the first occurrence of `item`.
* `sort()`: Sorts the list in place.

### Tuples

A **tuple** is an *immutable*, ordered collection of items. Once defined, the elements in a tuple cannot be modified, added, or removed. Tuples are useful for data that shouldn’t change, like fixed configuration values or coordinates.

```python
dimensions = (1920, 1080)  # Define a tuple
print(dimensions[0])  # Access the first element: Output: 1920
```

#### Why use tuples?

* Tuples are memory-efficient compared to lists.
* Useful when you want a constant, fixed-size collection of data.

### Dictionaries

A **dictionary** is an unordered collection of key-value pairs. Each key is unique and used to store and retrieve data efficiently. Dictionaries are ideal for mapping relationships, such as a user’s name to their profile data or an item to its price.

```python
person = {'name': 'Jazmine', 'age': 30}  # Define a dictionary
print(person['name'])  # Output: Jazmine
person['email'] = 'jazmine@example.com'  # Add a new key-value pair
```

#### Key Dictionary Methods

* `keys()`: Returns a list of keys in the dictionary.
* `values()`: Returns a list of values.
* `get(key)`: Returns the value associated with `key`, or `None` if `key` is not found.

### Sets

A **set** is an unordered collection of unique elements. Sets are useful for removing duplicates from a list or performing mathematical set operations like union, intersection, and difference.

```python
unique_numbers = {1, 2, 3, 3, 4}  # Define a set (duplicates are ignored)
unique_numbers.add(5)  # Add a new item
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
```

#### Common Set Operations

* `union()`: Returns a set containing all unique elements from both sets.
* `intersection()`: Returns elements common to both sets.
* `difference()`: Returns elements present in one set but not the other.

### Review Table: Lists, Tuples, Dictionaries, and Sets

Ok, let's review! Here's a table demonstrating the key differences between the four new terms we just learned:

| Data Structure | Ordered | Changeable (Mutable) | Allows Duplicates | Key-Value Pairs |
|----------------|---------|----------------------|-------------------|-----------------|
| **List**       | Yes     | Yes                 | Yes               | No              |
| **Tuple**      | Yes     | No                  | Yes               | No              |
| **Dictionary** | No      | Yes (Keys: No)      | Keys: No, Values: Yes | Yes           |
| **Set**        | No      | Yes                 | No                | No              |

### 2.1 Video: Lists, Tuples, Dictonaries, and Sets

[Video Description TBD]

**View the video here:** [LINK TBD]

### 2.1 Check for Understanding

**Question**: Which of the following statements about Python data structures is correct?

* A) Lists are immutable, and tuples are mutable.
* B) Sets allow duplicate elements.
* C) Dictionaries store data in key-value pairs and do not allow duplicate keys.
* D) Tuples are ordered and changeable.

<details>

<summary>Answer</summary>

**Answer**: C) Dictionaries store data in key-value pairs and do not allow duplicate keys.

</details>

## 2.2 File Handling

In Python, reading from and writing to text files is handled with the `open()` function. Text files are simple, containing plain text data, making them ideal for storing simple logs, configuration data, or notes.

#### Reading a Text File

To read a file, use `open()` with the `"r"` (read) mode and call `.read()`, `.readline()`, or .`readlines()` to get the content.

```python
with open('example.txt', 'r') as file:
    content = file.read()  # Read entire file
    print(content)
```

#### Writing to a Text File

To write to a file, open it in `"w"` (write) or `"a"` (append) mode. Writing mode will overwrite the file if it exists, while append mode will add to the file.

```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!")  # Write to the file
```

#### Additional Modes

* `"r+"`: Read and write
* `"a"`: Append to the file (keeps existing content).

### Reading and Writing CSV Files

CSV (Comma-Separated Values) files are commonly used to store tabular data, where each row is a new line, and each value is separated by a comma. Python’s built-in `csv` module makes it easy to work with these files.

#### Reading a CSV File

To read a CSV file, use `csv.reader()` and iterate through the rows.

```python
import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

#### Writing to a CSV File

To write to a CSV file, use `csv.writer()`. Each row should be a list or tuple representing a row in the CSV.

```python
import csv

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])  # Write header row
    writer.writerow(['Jazmine', 30, 'New York'])  # Write a data row
```

#### Additional Options

* `csv.DictReader()` and `csv.DictWriter()`: Use dictionaries to work with row data, which can make reading and writing more convenient when you have headers.

### 2.2 Video: Reading and Writing a CSV File

In this video, we'll demonstrate reading and writing to a real CSV file. After the video, practice reading and writing to a CSV file using the W3 Resource tutorial [here](https://www.w3resource.com/python-exercises/csv/index.php).

**View the video here:** [LINK TBD]

### 2.2 Check for Understanding

**Question**: What does the `"w"` mode do when opening a file in Python?

* A) Reads the file without making changes.
* B) Appends new data to the end of the file.
* C) Overwrites the file with new data, creating it if it doesn’t exist.
* D) Opens the file for reading and writing without overwriting.

<details>

<summary>Answer</summary>

**Answer**: C) Overwrites the file with new data, creating it if it doesn’t exist.

</details>

## 2.3 Introduction to Modules

In Python, a **module** is a file containing Python code, which can define functions, classes, and variables. Modules allow you to organize code logically, keeping related code together, and help avoid redundancy by making it reusable across different parts of a project.

For example, if you’re working on a project involving math calculations, you could create a module `math_utils.py` to hold custom math functions, making your main program file cleaner and easier to maintain.

### Why Use Modules?

Modules help in several ways:

  1. **Code Organization**: Breaks up large codebases into smaller, more manageable files.
  2. **Reusability**: Commonly used code can be stored in a module and imported wherever needed.
  3. **Namespace Management**: Modules allow you to separate code into different namespaces, avoiding conflicts between variables and functions with the same name.
  4. **Built-in Functionality**: Python’s standard library includes many modules that provide pre-built functionality (like math operations, file handling, and more), so you don’t have to reinvent the wheel.

### Importing Modules

You can import modules using the `import` statement, either as a whole or by importing specific functions or classes.

#### Importing an Entire Module

You can import a module and use its functions by prefixing them with the module name:

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

#### Importing Specific Functions or Classes

To import specific parts of a module, use `from <module> import <name>`:

```python
from math import sqrt
print(sqrt(16))  # Output: 4.0
```

#### Using Aliases

If a module has a long name, you can give it an alias with the `as` keyword:

```python
import pandas as pd
df = pd.DataFrame({'Name': ['Jazmine', 'Luis'], 'Age': [30, 35]})
```

### Python Standard Library and External Libraries

Python’s **standard library** is packed with built-in modules for handling everything from file I/O and math operations to data serialization and date/time management. For example:

* `datetime` for working with dates and times.
* `json` for handling JSON data.
* `os` for interacting with the operating system.

You can install and use **external libraries** with the `pip` package manager. External libraries are modules that add more functionality not included in the standard library, such as `requests` for HTTP requests or `numpy` for numerical operations.

#### Installing and Importing External Libraries

To install a library, use:

```bash
pip install requests
```

Then, import and use it like any other module:

```python
import requests
response = requests.get('https://api.example.com/data')
print(response.json())
```

#### Example: Creating and Importing a Custom Module

Suppose you create a file called `greetings.py` with a function:

```python
# greetings.py
def say_hello(name):
    return f"Hello, {name}!"
```

Then, in another file, you can import and use it:

```python
from greetings import say_hello
print(say_hello("Luis"))  # Output: Hello, Luis!
```

Modules and libraries in Python offer flexibility and organization, making your code easier to manage, expand, and share across projects.

### 2.3 Video: Python Modules and Libraries

[Video Description TBD]

**View the video here:** [LINK TBD]

### 2.3 Check for Understanding

**Question**: Which of the following commands correctly imports only the sqrt function from the `math` module?

* A) `import sqrt from math`
* B) `from math import sqrt`
* C) `import math.sqrt`
* D) `import math as sqrt`

<details>

<summary>Answer</summary>

**Answer**: B) `from math import sqrt`

</details>

## 2.4 Keyboard Input

In Python, handling keyboard input is straightforward, making it easy to interact with users. The input() function is the main way to capture user input from the keyboard, which you can then use directly or store in a variable for further processing.

#### Using `input()`

The `input()` function displays a prompt (optional) and waits for the user to type something and press Enter. By default, `input()` captures the input as a string, so if you need it in another format (like an integer), you’ll have to convert it.

```python
name = input("Enter your name: ")  # Displays a prompt and waits for input
print(f"Hello, {name}!")  # Greets the user with their input
```

#### Converting Input Types

Since `input()` returns data as a string, you’ll often want to convert it for calculations or comparisons.

```python
age = input("Enter your age: ")  # Gets input as a string
age = int(age)  # Converts input to an integer
print(f"Next year, you will be {age + 1} years old.")
```

If the user types something that can’t be converted (e.g., entering "twenty" instead of "20"), this will raise an error. To handle this gracefully, you can use `try-except`:

```python
try:
    age = int(input("Enter your age: "))
    print(f"Next year, you will be {age + 1} years old.")
except ValueError:
    print("Please enter a valid number.")
```

### Example: Simple Calculator Using Keyboard Input

Here’s a basic example that combines multiple `input()` calls to create a calculator. Pay attention to this code, because you'll be creating a calculator in this week's assignment!

```python
# Simple calculator
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operation")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### 2.4 Video

[Video Description TBD]

**View the video here:** [LINK TBD]

### 2.4 Check for Understanding

**Question**: Which of the following statements about `input()` in Python is correct?

* A) `input()` captures user input and automatically converts it to an integer.
* B) `input()` displays a prompt and captures user input as a string by default.
* C) `input()` captures user input but only works with numbers.
* D) `input()` is used to output text to the console.

<details>

<summary>Answer</summary>

**Answer**: B) input() displays a prompt and captures user input as a string by default.

</details>

---
This content was created by Janet Zulu, Reid Russom, and CTD volunteers. To submit feedback, please fill out the [CTD Curriculum Feedback Form](https://airtable.com/apphJi94mO4Uc7a3k/pagD3WQmswgXJvgx3/form).

## 2.5 Working with the OS

The `os` module in Python provides a powerful interface for interacting with the operating system. It enables you to perform various tasks, including:

* File and directory manipulation
* Environment variable handling
* Running system commands

These functionalities are essential for automating processes and managing files within Python programs.

### Common os Module Functions

**Getting the Current Working Directory**

The `os.getcwd()` function retrieves the path of the current working directory (the directory from which your Python script is executing).

```python
import os
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")
```

**Changing the Current Working Directory**

You can change the current working directory using `os.chdir(path)`, where `path` specifies the directory you want to switch to.

```python
os.chdir('/path/to/your/folder')
print(f"New working directory: {os.getcwd()}")
```

**Listing Files in a Directory**

The `os.listdir()` function returns a list containing all files and folders within the specified directory.

```python
files = os.listdir('/path/to/your/folder')
print(f"Files in the directory: {files}")
```

**Creating and Removing Directories**

Use `os.mkdir()` to create a new directory and `os.rmdir()` to remove an empty directory.

```python
# Create a new directory
os.mkdir('new_folder')

# Remove the directory
os.rmdir('new_folder')
```

*Note: If the directory isn't empty, you'll encounter an error. To remove a non-empty directory, use `shutil.rmtree()` from the `shutil` module.*

**Checking if a Path Exists**

Use `os.path.exists()` to verify if a file or directory exists at the specified path.

```python
if os.path.exists('some_file.txt'):
    print("The file exists.")
else:
    print("The file does not exist.")
```

**Getting File Information**

The `os.path` module provides functions to check file properties. For instance, use `os.path.isfile()` to determine if a path points to a file and `os.path.isdir()` to check if it's a directory.

```python
if os.path.isfile('some_file.txt'):
    print("This is a file.")
elif os.path.isdir('some_folder'):
    print("This is a folder.")
```

**Executing Shell Commands**

The `os.system()` function allows you to execute shell commands from within your Python program. You can leverage this functionality to run system commands like `ls` or `dir` to list files or execute other commands provided by your operating system.

```python
os.system('ls')  # For Linux/Mac
os.system('dir')  # For Windows
```

*Keep in mind that `os.system()` doesn't return the output of the command. If you need the output, consider using `subprocess.run()` instead.*

**Environment Variables**

You can access environment variables using `os.environ`. For example, to retrieve the `PATH` environment variable:

```python
path_variable = os.environ.get('PATH')
print(path_variable)
```

---

## 2.6 Virtual Environments

Virtual environments are a cornerstone of Python development, particularly when managing dependencies and isolating project environments. A virtual environment creates an isolated Python environment, enabling you to have project-specific dependencies that won't interfere with other projects or system-wide Python packages.

### Why Use Virtual Environments?

* **Isolation**: Virtual environments ensure that each project has its own set of dependencies, preventing version conflicts.
* **Reproducibility**: Virtual environments make it simpler to reproduce the exact setup for a project on another machine.
* **Dependency Management**: You can install and update packages without affecting other projects or your system's Python installation.

### Setting Up a Virtual Environment

1. **Install `virtualenv` (optional)**

   While Python 3.3+ comes with the `venv` module for creating virtual environments, some users prefer using `virtualenv` for additional features. To install it:

   ```bash
   pip install virtualenv
   ```

2. **Create a Virtual Environment**

   You can create a virtual environment using either `venv` (built-in module) or `virtualenv` (third-party package).

   - **Using `venv`**:

     ```bash
     python3 -m venv myenv
     ```

     This command creates a directory named `myenv` that contains the virtual environment.

   - **Using `virtualenv`**:

     ```bash
     virtualenv myenv
     ```

   **In both cases, `myenv` is the directory where the isolated Python environment will live.**

3. **Activating the Virtual Environment**

   To activate the virtual environment, use the following commands:

   * **Windows:**

     ```bash
     myenv\Scripts\activate
     ```

   * **Mac/Linux:**

     ```bash
     source myenv/bin/activate
     ```

   Once activated, your terminal prompt will usually change to show the virtual environment's name, e.g., `(myenv)`.

4. **Installing Packages in the Virtual Environment**

   After activation, you can install packages as usual with `pip`. These packages will be installed inside the virtual environment, not globally.

   ```bash
   pip install requests
   ```

   This ensures that the `requests` package is available only in the current virtual environment.

5. **Deactivating the Virtual Environment**

   To exit the virtual environment and return to the global Python environment, simply run:

   ```bash
   deactivate
   ```

6. **Managing Dependencies with `requirements.txt`**

   To record all the dependencies installed in your virtual environment, use the `pip freeze` command to generate a `requirements.txt` file:

   ```bash
   pip freeze > requirements.txt
   ```

   This file can be used to recreate the environment on another machine:

   ```bash
   pip install -r requirements.txt
   ```

7. **Virtual Environment with IDEs**

   Many IDEs, like VS Code and PyCharm, allow you to configure the Python interpreter to use the virtual environment. This ensures that the IDE uses the correct Python environment with all the necessary packages installed.


## 2.7 Introduction to Modules

A module is a Python file containing functions, classes, or variables that can be reused in other files. Modules allow you to organize code into smaller, manageable pieces, promoting reusability and better project structure.

### Using Modules

**Importing a Module**

To use a module in your program, you use the `import` statement. This makes the functions, classes, and variables in the module available for use in your code.

**Example:**

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

# main.py
import my_module

print(my_module.greet("Janet"))  # Output: Hello, Janet!
```

**Importing Specific Functions or Variables**

Instead of importing the entire module, you can import only specific parts:

```python
from math import sqrt

print(sqrt(16))  # Output: 4.0
```

**Using Aliases**

To simplify references or avoid conflicts, you can assign an alias to a module or its components:

```python
import pandas as pd
df = pd.DataFrame({'Name': ['Janet', 'Luis'], 'Age': [25, 30]})
```

**Creating Your Own Modules**

You can create a custom module by writing Python code in a .py file. For example, save the following as `math_tools.py`:

```python
# math_tools.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Now, you can import and use it in another Python file:

```python
import math_tools

print(math_tools.add(2, 3))       # Output: 5
print(math_tools.multiply(4, 5)) # Output: 20
```

**Benefits of Modules**

* **Code Reusability:** Write code once, use it anywhere in your project.
* **Better Organization:** Divide code into smaller, logical pieces for better maintainability.
* **Simplifies Debugging:** Smaller modules are easier to test and isolate issues.

## 2.9 Creating and Using Packages

A package is a collection of related modules organized into a directory structure. A package typically contains an __init__.py file, which allows Python to treat the directory as a package.

### Package Structure

Here's an example of a simple package structure:

```
my_package/
    __init__.py         # Indicates that this is a package
    math_tools.py       # Module for math-related functions
    string_tools.py     # Module for string-related functions
```

### Creating the Package

**1. Create the Package Directory:**

Start by creating a folder for your package, e.g., `my_package/`.

**2. Add an __init__.py File:**

Create an empty `__init__.py` file inside the package directory. This file can also include code to initialize the package.

**3. Add Modules to the Package:**

Add your Python files (modules) to the package directory, e.g., `math_tools.py` and `string_tools.py`.

### Using the Package

**Importing a Module from a Package**

You can import specific modules from a package:

```python
from my_package import math_tools

print(math_tools.add(10, 20))  # Output: 30
```

**Importing All Modules**

You can import all modules at once using `*` (if configured in `__init__.py`):

```python
from my_package import *
```

### Advanced Packages

**Adding Code to __init__.py**

The `__init__.py` file can include initialization code or make specific modules available at the package level:

```python
# __init__.py
from .math_tools import add
from .string_tools import capitalize

# Now you can use:
import my_package

print(my_package.add(2, 3))         # Output: 5
print(my_package.capitalize("hi")) # Output: Hi
```

### Why Use Packages?

* **Code Organization:** Packages help manage large projects by grouping related modules.
* **Encapsulation:** Control which parts of your package are accessible to other code.
* **Modular Programming:** Encourages better software design by separating concerns.


