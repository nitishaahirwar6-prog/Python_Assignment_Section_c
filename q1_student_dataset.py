students = {
    101: {
        "name": "Asha",
        "marks": {"Math": 88, "Physics": 76, "Chem": 92}
    },
    102: {
        "name": "Ravi",
        "marks": {"Math": 35, "Physics": 58, "Chem": 64}
    },
    103: {
        "name": "Meena",
        "marks": {"Math": 72, "Physics": 81, "Chem": 69}
    }
}

while True:
    print("\n--- STUDENT DATABASE ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Show Student Record")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = int(input("Enter roll number: "))

        if roll in students:
            print("Duplicate roll number!")
        else:
            name = input("Enter student name: ")
            marks = {}

            while True:
                subject = input("Enter subject (or done): ")

                if subject.lower() == "done":
                    break

                score = int(input("Enter marks (0-100): "))

                if 0 <= score <= 100:
                    marks[subject] = score
                else:
                    print("Marks out of range!")

            students[roll] = {
                "name": name,
                "marks": marks
            }

            print("Student added successfully!")

    elif choice == "2":
        roll = int(input("Enter roll number: "))

        if roll in students:
            subject = input("Enter subject: ")
            score = int(input("Enter new marks: "))

            if 0 <= score <= 100:
                students[roll]["marks"][subject] = score
                print("Marks updated!")
            else:
                print("Invalid marks!")
        else:
            print("Student not found!")

    elif choice == "3":
        roll = int(input("Enter roll number: "))

        if roll in students:
            del students[roll]
            print("Student deleted!")
        else:
            print("Student not found!")

    elif choice == "4":
        roll = int(input("Enter roll number: "))

        if roll in students:
            print(students[roll])
        else:
            print("Student not found!")

    elif choice == "5":

        averages = {
            roll: round(
                sum(data["marks"].values()) /
                len(data["marks"]), 2
            )
            for roll, data in students.items()
            if data["marks"]
        }

        print("\nStudent Averages:")

        for roll, avg in averages.items():
            print(roll, "->", avg)

        if averages:
            topper = max(averages, key=averages.get)
            print("Topper:", students[topper]["name"])

        print("\nHighest Marks in Each Subject:")

        subjects = {
            sub
            for data in students.values()
            for sub in data["marks"]
        }

        for sub in sorted(subjects):
            highest = max(
                (data["marks"][sub], data["name"])
                for data in students.values()
                if sub in data["marks"]
            )
            print(sub, "->", highest)

        print("\nStudents Below 40:")

        for roll, data in students.items():
            if any(
                marks < 40
                for marks in data["marks"].values()
            ):
                print(data["name"])

        grades = {
            "A": [],
            "B": [],
            "C": [],
            "D": [],
            "F": []
        }

        for roll, avg in averages.items():

            if avg >= 90:
                grades["A"].append(students[roll]["name"])
            elif avg >= 75:
                grades["B"].append(students[roll]["name"])
            elif avg >= 60:
                grades["C"].append(students[roll]["name"])
            elif avg >= 40:
                grades["D"].append(students[roll]["name"])
            else:
                grades["F"].append(students[roll]["name"])

        print("\nGrade Wise Grouping:")
        print(grades)

    elif choice == "6":
        print("Program Ended!")
        break

    else:
        print("Invalid choice!")