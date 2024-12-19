
# **Advanced SQL and Database Integration**

---

## **Lesson Overview**

**Learning Objective**:  
Students will deepen their understanding of SQL by learning advanced techniques such as subqueries, complex `JOIN`s, aggregation with functions, and using the `HAVING` clause for conditional filtering.

---

## **Assignment Instructions**

### **Task 1: Understanding Subqueries**

1. **Problem Statement**:  
   Write a SQL query to find the highest-paid employee in each department using a subquery.

2. **Deliverable**:  
   - Submit the SQL query and a screenshot of the result from your database interface.
   - Optional: Write a Python script to execute the query using `sqlite3` and print the results.

---

### **Task 2: Complex JOINs**

1. **Problem Statement**:  
   - Create a table `Projects` with the following fields:
     - `id`: Primary Key.
     - `name`: Project Name.
     - `department`: Responsible Department.
   - Populate it with at least three projects.
   - Write a SQL query to list all employees working in departments responsible for a specific project.

2. **Deliverable**:  
   - Submit the `CREATE TABLE` and `INSERT` statements used for the `Projects` table.
   - Submit the SQL query and results.

4. **Bonus**:  
   Extend the query to include the employee's salary in the results.

---

### **Task 3: Aggregation**

1. **Problem Statement**:  
   Write a SQL query to calculate the following for each department:
   - Minimum salary.
   - Maximum salary.
   - Total number of employees.

2. **Deliverable**:  
   - Submit the SQL query and results.
   - Add sample data in the `Employees` table to test the query.

3. **Example**:  
   ```sql
   SELECT department_id, 
          MIN(salary) AS min_salary, 
          MAX(salary) AS max_salary, 
          COUNT(employee_id) AS num_employees
   FROM Employees
   GROUP BY department_id;
   ```

4. **Bonus**:  
   Write a Python script to execute the query and display the results.

---

### **Task 4: Aggregation with HAVING**

1. **Problem Statement**:  
   Write a SQL query to:
   - List all departments where the average salary exceeds 70,000.
   - Display the department manager.

2. **Deliverable**:  
   - Submit the SQL query and results.
   - Explain the purpose of the `HAVING` clause in your solution.

3. **Example**:  
   ```sql
   SELECT d.department_name, 
          d.manager_id, 
          AVG(e.salary) AS avg_salary
   FROM Departments AS d
   JOIN Employees AS e ON d.department_id = e.department_id
   GROUP BY d.department_id
   HAVING AVG(e.salary) > 70000;
   ```

4. **Bonus**:  
   Integrate the query into a Python script and add exception handling for database errors.

---

## **Data Requirements**

1. Students must **create and populate tables** for the tasks:
   - Example for `Employees`:  
     | id  | name   | salary   | department   | manager   |
     |------|--------|----------|--------------|-----------|
     | 1    | Alice  | 80000    | IT           | Bob       |
     | 2    | John   | 90000    | IT           | Bob       |
   - Example for `Projects`:  
     | id  | name               | department |
     |-----|--------------------|------------|
     | 1   | Website Redesign   | IT         |

2. Alternatively, students can use their own datasets if they ensure the data has sufficient variety.

---



## **ESubmission**

Combine all tasks into a single Python script that:
1. Creates the necessary tables.
2. Populates the tables with sample data.
3. Executes all queries sequentially.
4. Prints results in a formatted manner.

---

### **Resources**
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python `sqlite3` Library Documentation](https://docs.python.org/3/library/sqlite3.html)
```
