# Lesson 1 — Introduction to Python

Welcome to **Python Essentials** with Code the Dream!

## How to Follow This Content

* Start by reading the lesson's **learning objective** in the `Lesson Overview` section. Each weekly assignment will measure your skill related to the learning objective.
* Lessons are split into **subsections**, labeled like this: `1.1`, `1.2`, etc.
* Each subsection has a short **supplemental video** that will help you understand the content in that subsection.
* At the end of each subsection, you'll find a multiple-choice **"Check for Understanding"** question. Complete the question and review the material if your answer is not correct!
* After reading through the lesson content and correctly answering the "Check for Understanding" questions, complete the **Weekly Assignment**.

If you have questions at any point, ask a question in the `discussion` Slack channel or reach out to your mentor!
## 1.1 Setting up uour environment 

**Start by creating a .py file somewhere convenient on your local machine.** 

You can create this file manually or through an IDE like Visual Studio Code. 

* **To set up VS Code:** 
    * Download and install it from here: [https://code.visualstudio.com/] 

**Alternatively, you can use a Jupyter Notebook (with the .ipynb extension) or any notebook platform, such as Google Colab, to keep your classwork organized.**

* **If you're new to Jupyter Notebooks, here's a resource on how to get started with Jupyter Notebooks in VS Code:** [(https://code.visualstudio.com/docs/datascience/jupyter-notebooks)]
* **Google Colab can also be used for running Jupyter Notebooks in the cloud. [https://colab.research.google.com/]** 
## Lesson Overview

**Learning objective:** Students will learn the basics of Python programming, including variables, data types, operators, control flow statements, and functions. They will also practice debugging their code.

Topics:

* Python Basics: Variables, data types, data conversion, operators.
* Control Flow: Conditional statements (if, elif, else), loops (for, while).
* Functions: Defining and calling functions, parameters, and return values.
* Error Handling: Introduction to try, except for basic debugging.
* Basic Debugging: Using print statements or logging for debugging.

### Install Python

You can download Python from the official website: [python.org](https://www.python.org/downloads/).

Follow the installation instructions for your operating system:

1. **For Windows**:
   - Download the latest version of Python for Windows from the Python official website.
   - Run the installer and make sure to **check the box to "Add Python to PATH"** during the installation process. This ensures that Python and `pip` (Python's package manager) will be available in your command prompt or terminal.
   - Choose the **"Install Now"** option to install Python with default settings, or use **"Customize Installation"** for more control over installation options.

2. **For macOS**:
   - macOS typically comes with Python pre-installed. To ensure you are using Python 3, download the latest version of Python from [python.org](https://www.python.org/downloads/).
   - Follow the installation instructions. You can also use **Homebrew** to install Python by running the following command in the terminal:
     ```bash
     brew install python
     ```

3. **For Linux**:
   - Most Linux distributions come with Python pre-installed. To install or upgrade Python 3, you can use the package manager:
     - For **Debian/Ubuntu** systems:
       ```bash
       sudo apt update
       sudo apt install python3
       ```
     - For **Fedora**:
       ```bash
       sudo dnf install python3
       ```
     - For **Arch Linux**:
       ```bash
       sudo pacman -S python
       ```

4. **Verifying Python Installation**:
   After installation, you can verify that Python was installed correctly by opening a terminal or command prompt and running:
   
   ```bash
   python --version
Or for Python 3 (in case of multiple Python versions):
```
python3 --version
```
This should display the installed version of Python. For example, you might see:
```
Python 3.9.7
```


### Install pip

**Pip** is Python’s package installer, and it is included automatically with Python versions 3.4 and above. It allows you to easily install and manage Python libraries and packages from the Python Package Index (PyPI).

#### Verify if pip is installed:
To check if **pip** is installed, open a terminal or command prompt and type:

```bash
pip --version
```

If you're using **Python 3**, you might need to use `pip3` instead:

```bash
pip3 --version
```

This should display the installed version of pip. If pip is not installed or you encounter an error, you may need to reinstall Python and ensure that the box for **Add Python to PATH** is checked.

#### Upgrading pip:
If you already have pip installed but want to make sure it’s up to date, run the following command:

```bash
python -m pip install --upgrade pip
```

Or, for Python 3:

```bash
python3 -m pip install --upgrade pip
```

#### Using pip:
Once pip is installed, you can install Python packages by using the following command:

```bash
pip install package_name
```

Or, for Python 3:

```bash
pip3 install package_name
```

For example, to install the `requests` library (which allows you to make HTTP requests), you would use:

```bash
pip install requests
```

Or, for Python 3:

```bash
pip3 install requests
```
## 1.2 Python Basics 
### Data Types in Python

**Data types** tell Python what kind of data is stored in a variable. Common data types include:

* Integer (`int`): Whole numbers (e.g., 42, -3)
* Float (`float`): Decimal numbers (e.g., 3.14, -0.5)
* String (`str`): Text (e.g., "hello", "world")
* Boolean (`bool`): Represents True or False values

```python
is_student = True       # Boolean
balance = 1000.75       # Float
first_name = "Charlie"  # String
number_of_days = 7      # Integer
```

You can check the type of a variable using the `type()` function:

```python
print(type(balance))  # Output: <class 'float'>
```

### Data Conversion

Data conversion, or **type casting**, is the process of converting one data type to another. Python provides several built-in functions to make this easy. Common conversion functions include `int()`, `float()`, `str()`, and `bool()`. Notice that these conversion functions line up with the data types demonstrated in the previous section.

```python
# Convert a string to an integer
num_str = "42"
num_int = int(num_str)  # 42 (integer)

# Convert an integer to a float
num_float = float(num_int)  # 42.0 (float)

# Convert a number to a string
num_str_again = str(num_int)  # "42" (string)

# Convert to a Boolean
is_empty = not bool("")  # True 
is_non_zero = bool(5)  # True (non-zero numbers are considered True)
```

#### Why Convert Data Types?

Data conversion is helpful when you need to perform operations between incompatible types or display values in specific formats. For instance, combining a number with text requires converting the number to a string.

```python
# Without type conversion
age = 30
message = "I am " + age + " years old."  # "TypeError: can only concatenate str (not "int") to str"
```

```python
# With type conversion
age = 30
message = "I am " + str(age) + " years old."  # "I am 30 years old."
```

#### Implicit vs. Explicit Conversion

Python sometimes performs **implicit conversion** (automatic type conversion), such as when adding an integer and a float, the result is automatically a float. However, for more control, it’s usually better to use **explicit conversion** with the functions above.

```python
# Implicit conversion
result = 3 + 2.5  # 5.5 (float, because Python converts the integer to float)

# Explicit conversion
result = int(2.8) + 3  # 5 (integer, because we explicitly converted the float to int)
```

### Video 1.1: Data Types and Conversion

Learn how to work with data types in Python in our first video, which covers essential type conversions with `int()`, `float()`, `str()`, and `bool()`, practical examples of when to use them, and tips to avoid common pitfalls.

**Watch the video here.** [LINK TBD]

## 1.3 Operators in Python

**Operators** are special symbols that perform operations on variables and values. Some of the most commonly used operators are:

1. **Arithmetic Operators**: For mathematical calculations
   * `+` (addition): `3 + 2` → `5`
   * `-` (subtraction): `5 - 3` → `2`
   * `*` (multiplication): `4 * 2` → `8`
   * `/` (division): `9 / 3` → `3.0`
   * `//` (integer division): `9 // 3` → `3`
   * `%` (modulus, remainder): `7 % 3` → `1`
   * `**` (exponentiation): `2 ** 3` → 8

2. **Comparison Operators**: Compare two values and return a Boolean (`True` or `False`)
   * `==` (equal to): `5 == 5` → `True`
   * `!=` (not equal to): `5 != 4` → `True`
   * `<` (less than): `3 < 4` → `True`
   * `>` (greater than): `10 > 5` → `True`
   * `<=` (less than or equal to): `5 <= 5` → `True`
   * `>=` (greater than or equal to): `7 >= 3` → `True`

3. **Logical Operators**: Used to combine conditional statements
   * `and`: `True and False` → `False`
   * `or`: `True or False` → `True`
   * `not`: `not True` → `False`

Operators Examples:

```python
# Arithmetic
result = 10 + 5  # 15
remainder = 9 % 4  # 1

# Comparison
print(5 > 3)  # True

# Logical
print(True and False)  # False
```

## 1.4 Block Structure and Indentations 

