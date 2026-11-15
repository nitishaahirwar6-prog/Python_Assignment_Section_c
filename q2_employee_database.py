# Q2. Employee Database (Grouping and Aggregation)

employees = {
    "E1": {"name": "Karan", "dept": "IT", "salary": 60000},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000}
}

while True:

    print("\n--- EMPLOYEE DATABASE ---")
    print("1. Add Employee")
    print("2. Update Salary")
    print("3. Delete Employee")
    print("4. Search Employee")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            print("Employee ID already exists!")

        else:
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))

            employees[emp_id] = {
                "name": name,
                "dept": dept,
                "salary": salary
            }

            print("Employee Added Successfully!")

    elif choice == "2":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            salary = float(input("Enter New Salary: "))
            employees[emp_id]["salary"] = salary
            print("Salary Updated Successfully!")

        else:
            print("Employee not found!")

    elif choice == "3":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            del employees[emp_id]
            print("Employee Deleted Successfully!")

        else:
            print("Employee not found!")

    elif choice == "4":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            print(employees[emp_id])

        else:
            print("Employee not found!")

    elif choice == "5":

        # Department-wise payroll and headcount
        departments = {}

        for emp in employees.values():
            dept = emp["dept"]

            data = departments.setdefault(
                dept, {"payroll": 0, "count": 0}
            )

            data["payroll"] += emp["salary"]
            data["count"] += 1

        print("\nDepartment-wise Reports:")

        for dept, data in departments.items():
            print(dept, "Payroll:", data["payroll"],
                  "Headcount:", data["count"])

        # Highest paid employee in each department
        print("\nHighest Paid Employee:")

        for dept in departments:
            highest = max(
                (e for e in employees.values() if e["dept"] == dept),
                key=lambda e: e["salary"]
            )

            print(dept, "->", highest["name"])

        # Employees sorted by salary
        print("\nEmployees Sorted by Salary:")

        sorted_employees = sorted(
            employees.items(),
            key=lambda x: x[1]["salary"],
            reverse=True
        )

        for emp_id, emp in sorted_employees:
            print(emp_id, emp["name"], emp["salary"])

        # 10% raise using dictionary comprehension
        # Original dictionary remains unchanged.

        raised_salaries = {
            emp_id: emp["salary"] * 1.10
            for emp_id, emp in employees.items()
            if emp["salary"] < 50000
        }

        print("\n10% Salary Raise:")
        print(raised_salaries)

        # Department with highest average salary
        averages = {
            dept: data["payroll"] / data["count"]
            for dept, data in departments.items()
        }

        highest_avg = max(averages, key=averages.get)

        print("\nHighest Average Salary:")
        print(highest_avg, averages[highest_avg])

    elif choice == "6":
        print("Program Ended!")
        break

    else:
        print("Invalid Choice!")