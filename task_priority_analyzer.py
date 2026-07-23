"""
Task Priority Analyzer
----------------------
File: task_priority_analyzer.py

Features
--------
✔ Task Creation
✔ Priority Score Calculation
✔ Urgency Analysis
✔ Importance Analysis
✔ Due Date Analysis
✔ Estimated Time Analysis
✔ Priority Classification
✔ Task Summary
"""

from datetime import datetime


class TaskPriorityAnalyzer:

    def __init__(self):

        self.tasks = []

    # ---------------------------------
    # Calculate Days Remaining
    # ---------------------------------
    def days_remaining(self, due_date):

        try:

            today = datetime.today().date()

            due = datetime.strptime(due_date, "%Y-%m-%d").date()

            return (due - today).days

        except:

            return None

    # ---------------------------------
    # Calculate Priority Score
    # ---------------------------------
    def calculate_priority(self, importance, urgency,
                           estimated_hours, due_date):

        score = 0

        # Importance
        if importance.lower() == "high":
            score += 40
        elif importance.lower() == "medium":
            score += 25
        else:
            score += 10

        # Urgency
        if urgency.lower() == "high":
            score += 30
        elif urgency.lower() == "medium":
            score += 20
        else:
            score += 10

        # Due Date
        days = self.days_remaining(due_date)

        if days is not None:

            if days <= 1:
                score += 20

            elif days <= 3:
                score += 15

            elif days <= 7:
                score += 10

        # Estimated Hours
        if estimated_hours >= 8:
            score += 10

        elif estimated_hours >= 4:
            score += 5

        return min(score, 100)

    # ---------------------------------
    # Priority Level
    # ---------------------------------
    def priority_level(self, score):

        if score >= 85:
            return "Critical"

        elif score >= 70:
            return "High"

        elif score >= 50:
            return "Medium"

        return "Low"

    # ---------------------------------
    # Add Task
    # ---------------------------------
    def add_task(self,
                 title,
                 importance,
                 urgency,
                 estimated_hours,
                 due_date):

        score = self.calculate_priority(
            importance,
            urgency,
            estimated_hours,
            due_date
        )

        task = {

            "Title": title,
            "Importance": importance,
            "Urgency": urgency,
            "Estimated Hours": estimated_hours,
            "Due Date": due_date,
            "Priority Score": score,
            "Priority": self.priority_level(score)

        }

        self.tasks.append(task)

        return task

    # ---------------------------------
    # Highest Priority Tasks
    # ---------------------------------
    def highest_priority(self):

        if not self.tasks:
            return []

        return sorted(
            self.tasks,
            key=lambda task: task["Priority Score"],
            reverse=True
        )

    # ---------------------------------
    # Summary
    # ---------------------------------
    def summary(self):

        summary = {

            "Total Tasks": len(self.tasks),
            "Critical":
                sum(
                    task["Priority"] == "Critical"
                    for task in self.tasks
                ),
            "High":
                sum(
                    task["Priority"] == "High"
                    for task in self.tasks
                ),
            "Medium":
                sum(
                    task["Priority"] == "Medium"
                    for task in self.tasks
                ),
            "Low":
                sum(
                    task["Priority"] == "Low"
                    for task in self.tasks
                )

        }

        return summary

    # ---------------------------------
    # Display Task
    # ---------------------------------
    def display_task(self, task):

        print("\n========== TASK ==========\n")

        for key, value in task.items():

            print(f"{key:<18}: {value}")

    # ---------------------------------
    # Display Summary
    # ---------------------------------
    def display_summary(self):

        report = self.summary()

        print("\n========== SUMMARY ==========\n")

        for key, value in report.items():

            print(f"{key:<15}: {value}")

    # ---------------------------------
    # Display All Tasks
    # ---------------------------------
    def display_all_tasks(self):

        if not self.tasks:

            print("\nNo tasks available.")

            return

        print("\n========== TASK LIST ==========\n")

        for index, task in enumerate(
                self.highest_priority(), start=1):

            print(f"Task {index}")

            print("-" * 35)

            for key, value in task.items():

                print(f"{key:<18}: {value}")

            print()


# ---------------------------------
# Example
# ---------------------------------

if __name__ == "__main__":

    analyzer = TaskPriorityAnalyzer()

    while True:

        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. View Summary")
        print("4. Exit")

        choice = input("\nChoice: ")

        if choice == "1":

            title = input("Task Title: ")

            importance = input(
                "Importance (High/Medium/Low): "
            )

            urgency = input(
                "Urgency (High/Medium/Low): "
            )

            hours = float(
                input("Estimated Hours: ")
            )

            due = input(
                "Due Date (YYYY-MM-DD): "
            )

            task = analyzer.add_task(
                title,
                importance,
                urgency,
                hours,
                due
            )

            analyzer.display_task(task)

        elif choice == "2":

            analyzer.display_all_tasks()

        elif choice == "3":

            analyzer.display_summary()

        elif choice == "4":

            print("\nThank you for using Task Priority Analyzer.")

            break

        else:

            print("\nInvalid choice.")