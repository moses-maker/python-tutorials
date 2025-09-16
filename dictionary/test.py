import sys
"""
5. Write a function that prompts the user for the average temperature for each day of the week and
 returns a dictionary containing the entered information.

recordings = {}

for x in range(0,7):
    day = input("Enter the Day e.g.(mon, Tue, Wed, Thur, Fri, Sat, Sun) When done type 'exit'?")
    temperature = int(input("Enter the tempearture in celcius?"))
    recordings.update({day:temperature})
    print(recordings)
print(recordings)
"""

information = {}

for c in range(0,6):
    e = c + 1
    salary = "salary"
    id = "employee number"
    print(f"Employee {e}")
    employee_name = input("Enter employee name?")
    employee_id = int(input("Enter employee id?"))
    employee_salary = int(input("Enter employee salary?"))
    information.update({employee_name:{id:employee_id, salary:employee_salary}})
    print(information)






