# List 3

## Person class
Write a Python program to create a person class. 
Include attributes like name, country and date of birth. 
Implement a method to calculate the person's age. 
No need for advanced stuff, subtracting from the current year will suffice. 

## Bank Account class
Write a Python class to represent a bank account with attributes like:
- `account_number`, `balance`, `date_of_opening` and `customer_name`,
- and methods like `deposit`, `withdraw`, and `check_balance`.

## Employee class
Write a Python class Employee with attributes like:
- `emp_id`, `emp_name`, `emp_salary`, and `emp_department`,
- and methods like `calculate_salary`, `assign_department`, and `print_details`.

Sample Employee Data:

- "ADAMS", "E7876", 50000, "ACCOUNTING"

- "JONES", "E7499", 45000, "RESEARCH"

- "MARTIN", "E7900", 50000, "SALES"

- "SMITH", "E7698", 55000, "OPERATIONS"

1. `assign_department` method changes the department of an employee.

2. `print_details` method prints the details of an employee.

3. `calculate_salary` method takes two arguments: salary and hours_worked, 
which is the number of hours worked by the employee. 
If the number of hours worked is more than 50, the method computes overtime 
and adds it to the salary. Overtime is calculated using the following formula:
```text
overtime = hours_worked - 50
overtime_amount = (overtime * (salary / 50))
```

## Shape class (inheritance)
Write a Python program to create a class that represents a shape. 
Include methods to calculate its area and perimeter. 
Implement subclasses for different shapes like circle, triangle, and square.

## Sine wave sampling
Write a program that generates a set of samples of a sine wave. 

The parameters are as follows: 
- Frequency: last 2 digits of a 6 digit number [Hz] (if it is '00' then use '01'),
- Sampling Frequency: 48 [kHz],
- Acquisition time: 2 [s],
- Amplitude: 2.

It should be realized as a class which stores the sine wave, 
has a method to generate sine wave samples with chosen parameters, 
plotting the sine wave as well as returning samples of downsampled wave.

Plot both sets on one figure for comparison. 

Hint – use numpy and matplotlib libraries.

## Player class (interactive Scrabble calculator)
Write a program with the same functionality as in [List 1](https://github.com/lysolaka/qd-python/blob/main/list1/tasks.md#scrabble-score-calculator). 
It should be realized as a `Player` class, where each player is a separate instance. 
Inside it stores the score of the player and has a method for calculating 
the score of a given word. Make a simple text UI.
