import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# STUDENT CLASS


class Student:

    def __init__(self, roll_no, name, python, dbms, maths, networking):
        self.roll_no = roll_no
        self.name = name
        self.python = python
        self.dbms = dbms
        self.maths = maths
        self.networking = networking

    def total_marks(self):
        return self.python + self.dbms + self.maths + self.networking

    def percentage(self):
        return self.total_marks() / 4

    def grade(self):

        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"



# ADD STUDENT


students = []


def add_student():

    print("\n========== ADD STUDENT ==========")

    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")

    python = float(input("Enter Python Marks: "))
    dbms = float(input("Enter DBMS Marks: "))
    maths = float(input("Enter Mathematics Marks: "))
    networking = float(input("Enter Networking Marks: "))

    # Validate marks
    marks = [python, dbms, maths, networking]

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Marks must be between 0 and 100.")
        return

    student = Student(
        roll_no,
        name,
        python,
        dbms,
        maths,
        networking
    )

    students.append(student)

    print("Student added successfully!")


# DISPLAY ALL STUDENTS


def display_students():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    print("\n================ STUDENT REPORT ================")

    print(
        f"{'Roll':<8}"
        f"{'Name':<15}"
        f"{'Python':<10}"
        f"{'DBMS':<10}"
        f"{'Maths':<10}"
        f"{'Network':<10}"
        f"{'Total':<10}"
        f"{'Percentage':<12}"
        f"{'Grade':<8}"
    )

    print("-" * 103)

    for student in students:

        print(
            f"{student.roll_no:<8}"
            f"{student.name:<15}"
            f"{student.python:<10.1f}"
            f"{student.dbms:<10.1f}"
            f"{student.maths:<10.1f}"
            f"{student.networking:<10.1f}"
            f"{student.total_marks():<10.1f}"
            f"{student.percentage():<12.2f}"
            f"{student.grade():<8}"
        )


# CREATE PANDAS DATAFRAME


def create_dataframe():

    data = []

    for student in students:

        data.append({
            "Roll No": student.roll_no,
            "Name": student.name,
            "Python": student.python,
            "DBMS": student.dbms,
            "Maths": student.maths,
            "Networking": student.networking,
            "Total": student.total_marks(),
            "Percentage": student.percentage(),
            "Grade": student.grade()
        })

    return pd.DataFrame(data)



# NUMPY SUBJECT ANALYSIS


def numpy_analysis():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    python_marks = np.array([s.python for s in students])
    dbms_marks = np.array([s.dbms for s in students])
    maths_marks = np.array([s.maths for s in students])
    networking_marks = np.array([s.networking for s in students])

    print("\n========== NUMPY ANALYSIS ==========")

    print("\nSubject Average Marks:")

    print("Python      :", np.mean(python_marks))
    print("DBMS        :", np.mean(dbms_marks))
    print("Mathematics :", np.mean(maths_marks))
    print("Networking  :", np.mean(networking_marks))

    print("\nHighest Marks:")

    print("Python      :", np.max(python_marks))
    print("DBMS        :", np.max(dbms_marks))
    print("Mathematics :", np.max(maths_marks))
    print("Networking  :", np.max(networking_marks))

    print("\nLowest Marks:")

    print("Python      :", np.min(python_marks))
    print("DBMS        :", np.min(dbms_marks))
    print("Mathematics :", np.min(maths_marks))
    print("Networking  :", np.min(networking_marks))



# CLASS PERFORMANCE


def class_analysis():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    df = create_dataframe()

    print("\n========== CLASS ANALYSIS ==========")

    print("Class Average Percentage:",
          round(df["Percentage"].mean(), 2))

    print("Highest Percentage:",
          round(df["Percentage"].max(), 2))

    print("Lowest Percentage:",
          round(df["Percentage"].min(), 2))

    topper_index = df["Percentage"].idxmax()

    print("Topper:",
          df.loc[topper_index, "Name"])

    print("\nGrade Distribution:")

    print(df["Grade"].value_counts())



# PANDAS DATA ANALYSIS


def pandas_analysis():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    df = create_dataframe()

    print("\n========== PANDAS DATAFRAME ==========")

    print(df)

    print("\nStudents with percentage above 75:")

    result = df[df["Percentage"] > 75]

    print(result[["Roll No", "Name", "Percentage", "Grade"]])



# BAR CHART


def bar_chart():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    df = create_dataframe()

    plt.figure(figsize=(10, 6))

    plt.bar(df["Name"], df["Percentage"])

    plt.xlabel("Students")
    plt.ylabel("Percentage")
    plt.title("Student Percentage Analysis")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()



# SUBJECT-WISE BAR CHART


def subject_chart():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    df = create_dataframe()

    subjects = [
        "Python",
        "DBMS",
        "Maths",
        "Networking"
    ]

    averages = [
        df["Python"].mean(),
        df["DBMS"].mean(),
        df["Maths"].mean(),
        df["Networking"].mean()
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(subjects, averages)

    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.title("Subject-wise Average Marks")

    plt.tight_layout()

    plt.show()


# PIE CHART


def pie_chart():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    df = create_dataframe()

    grade_counts = df["Grade"].value_counts()

    plt.figure(figsize=(7, 7))

    plt.pie(
        grade_counts.values,
        labels=grade_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Grade Distribution")

    plt.show()



# HISTOGRAM


def histogram():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    df = create_dataframe()

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Percentage"],
        bins=5,
        edgecolor="black"
    )

    plt.xlabel("Percentage")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Student Percentage")

    plt.show()



# SEARCH STUDENT


def search_student():

    if len(students) == 0:
        print("\nNo student data available.")
        return

    roll_no = int(input("\nEnter Roll Number to search: "))

    found = False

    for student in students:

        if student.roll_no == roll_no:

            print("\nStudent Found!")

            print("Roll Number :", student.roll_no)
            print("Name        :", student.name)
            print("Python      :", student.python)
            print("DBMS        :", student.dbms)
            print("Mathematics :", student.maths)
            print("Networking  :", student.networking)
            print("Total       :", student.total_marks())
            print("Percentage  :", student.percentage())
            print("Grade       :", student.grade())

            found = True
            break

    if not found:
        print("Student not found.")



# MAIN MENU


def main():

    while True:

        print("\n")
        print("==============================================")
        print("       STUDENT MARKS & PERFORMANCE ANALYZER")
        print("==============================================")

        print("1. Add Student")
        print("2. Display Student Report")
        print("3. Search Student")
        print("4. NumPy Subject Analysis")
        print("5. Class Performance Analysis")
        print("6. Pandas Data Analysis")
        print("7. Student Percentage Bar Chart")
        print("8. Subject-wise Average Chart")
        print("9. Grade Distribution Pie Chart")
        print("10. Percentage Histogram")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            numpy_analysis()

        elif choice == "5":
            class_analysis()

        elif choice == "6":
            pandas_analysis()

        elif choice == "7":
            bar_chart()

        elif choice == "8":
            subject_chart()

        elif choice == "9":
            pie_chart()

        elif choice == "10":
            histogram()

        elif choice == "0":
            print("\nThank you for using Student Performance Analyzer!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# PROGRAM START


if __name__ == "__main__":
    main()