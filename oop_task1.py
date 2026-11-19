
import csv

# 1. Function using *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


print("Bonus:", bonus(50000, 0.1, 500, 1000, cap=6000))


# 2. Custom exception
class InvalidSalaryError(Exception):
    pass


# 3. Employee class
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(
                f"Invalid salary: {salary}"
            )

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# 4. Manager inheritance
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Manager: {self.name}, "
            f"Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )


# 5. Create Employee and Manager objects
emp = Employee("Arun", 30000)
mgr = Manager("Priya", 45000, 5)

print(emp.get_details())
print("Annual Salary:", emp.annual_salary())
print(mgr.get_details())


# 6. Handle custom exception
try:
    invalid_emp = Employee("Test", -500)

except InvalidSalaryError as e:
    print("Error:", e)

finally:
    print("Transaction finished")


# 7. Read employees.csv
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

# Convert salary into integer
for employee in employees:
    employee["salary"] = int(employee["salary"])


# 8. List comprehension:
# Names with salary above 50000
above_50000 = [
    emp["name"]
    for emp in employees
    if emp["salary"] > 50000
]

print("Above 50000:", above_50000)


# 9. Map and lambda:
# Add 10% salary raise
raised_salaries = list(
    map(
        lambda emp: {
            "name": emp["name"],
            "new_salary": emp["salary"] * 1.10
        },
        employees
    )
)

print("10% Salary Raise:", raised_salaries)


# 10. Filter:
# Keep Chennai employees
chennai_employees = list(
    filter(
        lambda emp: emp["city"] == "Chennai",
        employees
    )
)

chennai_names = [
    emp["name"] for emp in chennai_employees
]

print("Chennai:", chennai_names)


# 11. For loop with continue and break
print("Loop output:")

salaries = [30000, 0, 45000, 60000, 90000, 52000]

for salary in salaries:

    if salary == 0:
        continue

    if salary > 85000:
        break

    print(salary)
