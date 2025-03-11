
# Task 2: Read a CSV File
import csv
import traceback
def read_employees():
    try:
        kv = {}
        rows = []
        # read the csv file employees.csv
        first_row = True
        with open('../csv/employees.csv', 'r') as csvfh:
            reader = csv.reader(csvfh)
            for row in reader:
                if first_row:
                    first_row = False
                    kv['fields'] = row
                else:
                    rows.append(row)
        kv['rows'] = rows
        return kv
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")

employees = read_employees()
print('Task2:\n', employees)

# Task 3: Find the Column Index
def column_index(heading):
    return employees['fields'].index(heading)

employee_id_column = column_index('employee_id')
print('Task2:\n', f'Employee_id_column: {employee_id_column}')

# Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_index = column_index('first_name')
    return employees['rows'][row_number][first_name_index]

print('Task 4:\n', first_name(3))

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):

    # test function for filter
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    try:
        # find the 
        matches=list(filter(employee_match, employees["rows"]))

        return matches
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    
print('task 5:\n', employee_find(3))

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):

    try:
        # find the 
        matches=list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

        return matches
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    try:
        employees['rows'].sort(key=lambda row: row[column_index('last_name')])
        return employees['rows']
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

print('Task 7:\n', sort_by_last_name())

# Task 8: Create a dict for an Employee
def employee_dict(row):

    try:
        keys = employees['fields']
        return dict(zip(keys[1:], row[1:]))
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

print('Task 8:\n', employee_dict(employees['rows'][0]))

# Task 9: A dict of dicts, for All Employees
# The keys in the dict are the employee_id values from the rows in the employees dict.
# For each key, the value is the employee dict created for that row.  (Use the employee_dict function you created in task 8.)
def all_employees_dict():

    try:
        employees_dict = {}
        for row in employees['rows']:
            id = row[0]
            employees_dict[id] = employee_dict(row)
        return employees_dict
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

print('Task 9:\n', all_employees_dict())

# Task 10: Use the os Module
import os
def get_this_value():
    return os.getenv('THISVALUE')

print('Task 10:\n', get_this_value())

# Task 11: Creating Your Own Module
import custom_module
def set_that_secret(secret):
    custom_module.set_secret(secret)

set_that_secret('foo')
print('Task 11:\n', custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes_file(file_path): # read one minutes file
    try:
        kv = {}
        rows = []
        # read the csv file employees.csv
        first_row = True
        with open(file_path, 'r') as csvfh:
            reader = csv.reader(csvfh)
            for row in reader:
                if first_row:
                    first_row = False
                    kv['fields'] = row
                else:
                    rows.append(tuple(row))
        kv['rows'] = rows
        return kv
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")

def read_minutes():
    try:
        return read_minutes_file('../csv/minutes1.csv'), read_minutes_file('../csv/minutes2.csv')
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")

minutes1, minutes2 = read_minutes()
print('Task12:\n', minutes1, minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    try:
        return set(minutes1['rows']).union(set(minutes2['rows']))
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")

minutes_set = create_minutes_set()
print('Task13:\n', minutes_set)

# Task 14: Convert to datetime
from datetime import datetime
def create_minutes_list():
    try:
        minutes_list = list(minutes_set)
        converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
        return converted_list
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")

minutes_list = create_minutes_list()
print('Task14:\n', minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    try:
        # sort the minutes_list in ascending order of datetime
        minutes_list.sort(key=lambda x: x[1])

        # convert datetimes back to strings
        converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

        # write the result out as a cvs
        with open('./minutes.csv', 'w') as csvwfh:
            writer = csv.writer(csvwfh)
            writer.writerow(minutes1['fields'])  # Write header row
            for row in converted_list:
                writer.writerow(row)  # Write a data row

        return converted_list
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")

print('Task 15:\n', write_sorted_list())





   










