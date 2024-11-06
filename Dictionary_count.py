"""
Nested Dict total count using FOR Loop:
"""

employee_data = {
    'employee1': {
        'name': 'John Doe',
        'age': 30,
        'department': 'HR'
    },
    'employee2': {
        'name': 'Jane Smith',
        'age': 25,
        'department': 'Finance'
    },
    'employee3': {
        'name': 'Emily Johnson',
        'age': 35,
        'department': 'IT'
    }
}

# Initialize total age
total_age = 0

# Iterate through the employee data and sum ages
for employee in employee_data.values():
    # print(employee['age'])
    total_age += employee['age']

print("Total age of all employees:", total_age)  
