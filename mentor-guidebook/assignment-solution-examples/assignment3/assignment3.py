import numpy as np
import pandas as pd

# Task 1

# Create a DataFrame from a dictionary:
task1_dict = {  'Name': ['Alice', 'Bob', 'charlie'], 
                'Age': [25, 30, 35], 
                'City': ['New York', 'Los Angeles', 'Chicago']}
task1_data_frame = pd.DataFrame(task1_dict)
print(task1_data_frame)

# add a column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# increment the age column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

# save to a csv names employees.csv
task1_older.to_csv('employees.csv', index=False)

# Task 2

# Load the employees.csv file into a dataFrame and assign it to task2_employees
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)
print(task2_employees.columns)
print(len(task2_employees.columns))
print(task2_employees.shape)

# Load additional_eomployees.json into json_employees
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

# Add the new employees to the DataFrame read from csv
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)
print(more_employees.shape)
print(more_employees.head(3))

# Task 3

# head
first_three = more_employees.head(3)
print(first_three)

#tail
last_two = more_employees.tail(2)
print(last_two)

#shape
employee_shape = more_employees.shape
print(employee_shape)

# info
print(more_employees.info())

print(more_employees.describe())
print(more_employees.select_dtypes(include=[np.number]).corr())

# Task 4
dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)
clean_data = dirty_data.copy()

# remove duplicates
clean_data.drop_duplicates(inplace=True)

# make sure Age is numeric
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

# Make sure Salary is numeric and fix known placeholders, cvt to NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

# Fill in missing numeric values
mean_age = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(mean_age)
median_salary = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)

# Convert hire date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')

# Standardize Name' and 'Department'
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

print(clean_data)





















