import tkinter as tk
from tkinter import ttk, messagebox

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

class StudentAnalyzerGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Marks & Performance Analyzer")
        self.root.geometry("1150x720")
        self.root.minsize(950, 600)

        self.root.configure(bg="#eef2f7")

        self.students = []

        self.create_header()
        self.create_input_section()
        self.create_buttons()
        self.create_student_table()
        self.create_status_bar()

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg="#17365d",
            height=85
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="STUDENT MARKS & PERFORMANCE ANALYZER",
            font=("Arial", 21, "bold"),
            fg="white",
            bg="#17365d"
        )

        title.pack(pady=(15, 3))

        subtitle = tk.Label(
            header,
            text="Student Records | Statistical Analysis | Data Visualization",
            font=("Arial", 10),
            fg="#dce6f1",
            bg="#17365d"
        )

        subtitle.pack()

    def create_input_section(self):

        container = tk.LabelFrame(
            self.root,
            text="Student Information",
            font=("Arial", 12, "bold"),
            bg="#eef2f7",
            padx=15,
            pady=12
        )

        container.pack(fill="x", padx=15, pady=12)

        self.entries = {}

        fields = [
            ("Roll Number", "roll"),
            ("Student Name", "name"),
            ("Python Marks", "python"),
            ("DBMS Marks", "dbms"),
            ("Mathematics Marks", "maths"),
            ("Networking Marks", "networking")
        ]

        for index, (label_text, key) in enumerate(fields):

            row = index // 3
            col = (index % 3) * 2

            label = tk.Label(
                container,
                text=label_text,
                font=("Arial", 10),
                bg="#eef2f7"
            )

            label.grid(
                row=row,
                column=col,
                sticky="w",
                padx=8,
                pady=8
            )

            entry = ttk.Entry(
                container,
                width=23,
                font=("Arial", 10)
            )

            entry.grid(
                row=row,
                column=col + 1,
                sticky="ew",
                padx=8,
                pady=8
            )

            self.entries[key] = entry

        for col in range(6):
            container.columnconfigure(col, weight=1)

    def create_buttons(self):

        frame = tk.Frame(
            self.root,
            bg="#eef2f7"
        )

        frame.pack(fill="x", padx=15, pady=5)

        buttons = [
            ("Add Student", self.add_student),
            ("Search Student", self.search_student),
            ("Class Analysis", self.class_analysis),
            ("NumPy Analysis", self.numpy_analysis),
            ("Pandas Analysis", self.pandas_analysis),
            ("Student Chart", self.student_chart),
            ("Subject Chart", self.subject_chart),
            ("Grade Pie Chart", self.pie_chart),
            ("Percentage Histogram", self.histogram),
            ("Clear Fields", self.clear_fields),
            ("Exit", self.exit_app)
        ]

        for index, (text, command) in enumerate(buttons):

            button = tk.Button(
                frame,
                text=text,
                command=command,
                font=("Arial", 9, "bold"),
                bg="#245b91",
                fg="white",
                activebackground="#3679b9",
                activeforeground="white",
                relief="flat",
                padx=8,
                pady=8,
                cursor="hand2"
            )

            button.grid(
                row=index // 6,
                column=index % 6,
                padx=4,
                pady=5,
                sticky="ew"
            )

        for col in range(6):
            frame.columnconfigure(col, weight=1)

    def create_student_table(self):

        frame = tk.LabelFrame(
            self.root,
            text="Student Records",
            font=("Arial", 12, "bold"),
            bg="#eef2f7",
            padx=10,
            pady=10
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        columns = (
            "Roll", "Name", "Python", "DBMS",
            "Maths", "Networking", "Total",
            "Percentage", "Grade"
        )

        self.tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            height=12
        )

        widths = {
            "Roll": 65,
            "Name": 150,
            "Python": 80,
            "DBMS": 80,
            "Maths": 80,
            "Networking": 100,
            "Total": 80,
            "Percentage": 100,
            "Grade": 65
        }

        for column in columns:

            self.tree.heading(
                column,
                text=column
            )

            self.tree.column(
                column,
                width=widths[column],
                anchor="center"
            )

        scrollbar_y = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=self.tree.yview
        )

        scrollbar_x = ttk.Scrollbar(
            frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scrollbar_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)


    def create_status_bar(self):

        self.status = tk.Label(
            self.root,
            text="Ready | Total Students: 0",
            bg="#17365d",
            fg="white",
            anchor="w",
            padx=12,
            pady=6
        )

        self.status.pack(fill="x")

    def create_dataframe(self):

        data = []

        for student in self.students:

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

    def refresh_table(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        for student in self.students:

            self.tree.insert(
                "",
                "end",
                values=(
                    student.roll_no,
                    student.name,
                    f"{student.python:.1f}",
                    f"{student.dbms:.1f}",
                    f"{student.maths:.1f}",
                    f"{student.networking:.1f}",
                    f"{student.total_marks():.1f}",
                    f"{student.percentage():.2f}%",
                    student.grade()
                )
            )

        self.status.config(
            text=f"Ready | Total Students: {len(self.students)}"
        )

    def add_student(self):

        try:

            roll_no = int(
                self.entries["roll"].get().strip()
            )

            name = self.entries["name"].get().strip()

            python = float(
                self.entries["python"].get().strip()
            )

            dbms = float(
                self.entries["dbms"].get().strip()
            )

            maths = float(
                self.entries["maths"].get().strip()
            )

            networking = float(
                self.entries["networking"].get().strip()
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Enter a valid roll number and numeric marks."
            )

            return

        if roll_no <= 0:

            messagebox.showerror(
                "Invalid Roll Number",
                "Roll number must be greater than zero."
            )

            return

        if not name:

            messagebox.showerror(
                "Missing Name",
                "Please enter the student's name."
            )

            return

        if any(
            not np.isfinite(mark) or mark < 0 or mark > 100
            for mark in [python, dbms, maths, networking]
        ):

            messagebox.showerror(
                "Invalid Marks",
                "Marks must be between 0 and 100."
            )

            return

        if any(
            student.roll_no == roll_no
            for student in self.students
        ):

            messagebox.showerror(
                "Duplicate Roll Number",
                "This roll number already exists."
            )

            return

        student = Student(
            roll_no,
            name,
            python,
            dbms,
            maths,
            networking
        )

        self.students.append(student)

        self.refresh_table()
        self.clear_fields()

        messagebox.showinfo(
            "Success",
            f"Student {name} added successfully!"
        )

    def clear_fields(self):

        for entry in self.entries.values():
            entry.delete(0, tk.END)

        self.entries["roll"].focus_set()


    def search_student(self):

        if not self.students:

            messagebox.showwarning(
                "No Records",
                "Please add a student first."
            )

            return

        dialog = tk.Toplevel(self.root)

        dialog.title("Search Student")
        dialog.geometry("350x150")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(
            dialog,
            text="Enter Roll Number:",
            font=("Arial", 11)
        ).pack(pady=(20, 8))

        entry = ttk.Entry(
            dialog,
            font=("Arial", 11)
        )

        entry.pack()
        entry.focus_set()

        def find_student():

            try:
                roll = int(entry.get().strip())

            except ValueError:

                messagebox.showerror(
                    "Invalid Input",
                    "Enter a valid roll number.",
                    parent=dialog
                )

                return

            for student in self.students:

                if student.roll_no == roll:

                    for item in self.tree.get_children():

                        values = self.tree.item(item, "values")

                        if int(values[0]) == roll:

                            self.tree.selection_set(item)
                            self.tree.focus(item)
                            self.tree.see(item)

                            break

                    messagebox.showinfo(
                        "Student Found",
                        f"Roll Number: {student.roll_no}\n"
                        f"Name: {student.name}\n"
                        f"Python: {student.python}\n"
                        f"DBMS: {student.dbms}\n"
                        f"Mathematics: {student.maths}\n"
                        f"Networking: {student.networking}\n"
                        f"Total: {student.total_marks():.1f}\n"
                        f"Percentage: {student.percentage():.2f}%\n"
                        f"Grade: {student.grade()}",
                        parent=dialog
                    )

                    dialog.destroy()
                    return

            messagebox.showinfo(
                "Not Found",
                "No student exists with this roll number.",
                parent=dialog
            )

        ttk.Button(
            dialog,
            text="Search",
            command=find_student
        ).pack(pady=15)

        entry.bind(
            "<Return>",
            lambda event: find_student()
        )

    def numpy_analysis(self):

        if not self.students:

            messagebox.showwarning(
                "No Records",
                "Please add student records first."
            )

            return

        subjects = {
            "Python": np.array(
                [s.python for s in self.students]
            ),
            "DBMS": np.array(
                [s.dbms for s in self.students]
            ),
            "Mathematics": np.array(
                [s.maths for s in self.students]
            ),
            "Networking": np.array(
                [s.networking for s in self.students]
            )
        }

        report = "NUMPY SUBJECT ANALYSIS\n\n"

        for subject, marks in subjects.items():

            report += (
                f"{subject}\n"
                f"  Average: {np.mean(marks):.2f}\n"
                f"  Highest: {np.max(marks):.2f}\n"
                f"  Lowest: {np.min(marks):.2f}\n\n"
            )

        messagebox.showinfo(
            "NumPy Analysis",
            report
        )

    def class_analysis(self):

        if not self.students:

            messagebox.showwarning(
                "No Records",
                "Please add student records first."
            )

            return

        df = self.create_dataframe()

        topper_index = df["Percentage"].idxmax()
        topper = df.loc[topper_index]

        grade_counts = (
            df["Grade"]
            .value_counts()
            .reindex(
                ["A+", "A", "B", "C", "D", "F"],
                fill_value=0
            )
        )

        report = (
            "CLASS PERFORMANCE ANALYSIS\n\n"
            f"Total Students: {len(df)}\n"
            f"Class Average: {df['Percentage'].mean():.2f}%\n"
            f"Highest Percentage: {df['Percentage'].max():.2f}%\n"
            f"Lowest Percentage: {df['Percentage'].min():.2f}%\n"
            f"Topper: {topper['Name']}\n"
            f"Topper Roll No: {int(topper['Roll No'])}\n\n"
            "GRADE DISTRIBUTION\n"
        )

        for grade, count in grade_counts.items():

            report += f"{grade}: {count} student(s)\n"

        messagebox.showinfo(
            "Class Analysis",
            report
        )

    def pandas_analysis(self):

        if not self.students:

            messagebox.showwarning(
                "No Records",
                "Please add student records first."
            )

            return

        df = self.create_dataframe()

        result = df[df["Percentage"] > 75]

        window = tk.Toplevel(self.root)

        window.title("Pandas Data Analysis")
        window.geometry("950x450")

        tk.Label(
            window,
            text="Students Scoring Above 75%",
            font=("Arial", 15, "bold")
        ).pack(pady=12)

        tk.Label(
            window,
            text=f"Total Records: {len(df)} | Above 75%: {len(result)}",
            font=("Arial", 10)
        ).pack(pady=5)

        text = tk.Text(
            window,
            font=("Consolas", 10),
            wrap="none"
        )

        scrollbar_y = ttk.Scrollbar(
            window,
            orient="vertical",
            command=text.yview
        )

        scrollbar_x = ttk.Scrollbar(
            window,
            orient="horizontal",
            command=text.xview
        )

        text.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        text.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(5, 0)
        )

        scrollbar_x.pack(fill="x", padx=10)

        text.insert(
            tk.END,
            "ALL STUDENT RECORDS\n\n"
        )

        text.insert(
            tk.END,
            df.to_string(index=False, float_format="%.2f")
        )

        text.insert(
            tk.END,
            "\n\nSTUDENTS ABOVE 75%\n\n"
        )

        if result.empty:

            text.insert(
                tk.END,
                "No students scored above 75%."
            )

        else:

            text.insert(
                tk.END,
                result[
                    ["Roll No", "Name", "Percentage", "Grade"]
                ].to_string(index=False)
            )

        text.config(state="disabled")

    def student_chart(self):

        if not self.students:

            messagebox.showwarning(
                "No Records",
                "Please add student records first."
            )

            return

        df = self.create_dataframe()

        plt.figure(figsize=(10, 6))

        plt.bar(
            df["Name"],
            df["Percentage"]
        )

        plt.xlabel("Students")
        plt.ylabel("Percentage")
        plt.title("Student Percentage Analysis")

        plt.ylim(0, 100)
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

   
    def subject_chart(self):

        if not self.students:

            messagebox.showwarning(
                "No Records",
                "Please add student records first."
            )

            return

        df = self.create_dataframe()

        subjects = [
            "Python",
            "DBMS",
            "Maths",
            "Networking"
        ]

        averages = [
            df[subject].mean()
            for subject in subjects
        ]

        plt.figure(figsize=(8, 5))

        plt.bar(
            subjects,
            averages
        )

        plt.xlabel("Subjects")
        plt.ylabel("Average Marks")
        plt.title("Subject-wise Average Marks")

        plt.ylim(0, 100)
        plt.tight_layout()

        plt.show()

    def pie_chart(self):

        if not self.students:

            messagebox.showwarning(
                "No Records",
                "Please add student records first."
            )

            return

        df = self.create_dataframe()

        grade_counts = (
            df["Grade"]
            .value_counts()
            .reindex(
                ["A+", "A", "B", "C", "D", "F"],
                fill_value=0
            )
        )

        grade_counts = grade_counts[
            grade_counts > 0
        ]

        plt.figure(figsize=(7, 7))

        plt.pie(
            grade_counts.values,
            labels=grade_counts.index,
            autopct="%1.1f%%"
        )

        plt.title("Grade Distribution")

        plt.tight_layout()
        plt.show()


    def histogram(self):

        if not self.students:

            messagebox.showwarning(
                "No Records",
                "Please add student records first."
            )

            return

        df = self.create_dataframe()

        plt.figure(figsize=(8, 5))

        plt.hist(
            df["Percentage"],
            bins=5,
            edgecolor="black"
        )

        plt.xlabel("Percentage")
        plt.ylabel("Number of Students")
        plt.title("Distribution of Student Percentage")

        plt.tight_layout()
        plt.show()

   
    def exit_app(self):

        answer = messagebox.askyesno(
            "Exit Application",
            "Are you sure you want to exit?"
        )

        if answer:
            self.root.destroy()


if __name__ == "__main__":

    root = tk.Tk()

    app = StudentAnalyzerGUI(root)

    root.mainloop()
