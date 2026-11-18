employees = {
    101: {"name": "Areen", "department": "IT", "salary": 30000},
    102: {"name": "Rahul", "department": "HR", "salary": 25000},
    103: {"name": "Amit", "department": "Finance", "salary": 40000}
}

print("Employee Details:", employees)

employees[104] = {"name": "Priya", "department": "IT", "salary": 35000}
print("After Adding:", employees)

employees[101]["salary"] = 45000
print("After Updating:", employees)

del employees[102]
print("After Deleting:", employees)

print("Employee IDs:", employees.keys())
print("Employee Values:", employees.values())
print("Employee Items:", employees.items())

eid = int(input("Enter Employee ID to search: "))

if eid in employees:
    print("Employee Found:", employees[eid])
else:
    print("Employee Not Found")

salary = int(input("Enter minimum salary: "))

high_salary = {
    id: details for id, details in employees.items()
    if details["salary"] > salary
}

print("Employees earning above", salary, ":", high_salary)
