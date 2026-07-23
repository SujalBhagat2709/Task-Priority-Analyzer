"""
Task Priority Studio
--------------------
Main file for Task Priority Analyzer.
"""

from task_priority_analyzer import TaskPriorityAnalyzer


class TaskPriorityStudio:

    def __init__(self):

        self.analyzer = TaskPriorityAnalyzer()

    # ---------------------------------
    # Add New Task
    # ---------------------------------
    def add_task(self):

        print("\n========== ADD TASK ==========\n")

        title = input("Task Title: ").strip()

        importance = input(
            "Importance (High/Medium/Low): "
        ).strip()

        urgency = input(
            "Urgency (High/Medium/Low): "
        ).strip()

        estimated_hours = float(
            input("Estimated Hours: ")
        )

        due_date = input(
            "Due Date (YYYY-MM-DD): "
        ).strip()

        task = self.analyzer.add_task(
            title,
            importance,
            urgency,
            estimated_hours,
            due_date
        )

        print("\nTask Added Successfully.")

        self.analyzer.display_task(task)

    # ---------------------------------
    # View All Tasks
    # ---------------------------------
    def view_tasks(self):

        self.analyzer.display_all_tasks()

    # ---------------------------------
    # Highest Priority Task
    # ---------------------------------
    def highest_priority(self):

        tasks = self.analyzer.highest_priority()

        if not tasks:

            print("\nNo tasks available.")

            return

        print("\n========== HIGHEST PRIORITY TASK ==========\n")

        self.analyzer.display_task(tasks[0])

    # ---------------------------------
    # View Summary
    # ---------------------------------
    def summary(self):

        self.analyzer.display_summary()

    # ---------------------------------
    # Menu
    # ---------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 50)
            print("        TASK PRIORITY ANALYZER")
            print("=" * 50)
            print("1. Add Task")
            print("2. View All Tasks")
            print("3. View Highest Priority Task")
            print("4. View Summary")
            print("5. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":

                self.add_task()

            elif choice == "2":

                self.view_tasks()

            elif choice == "3":

                self.highest_priority()

            elif choice == "4":

                self.summary()

            elif choice == "5":

                print("\nThank you for using Task Priority Analyzer.")
                break

            else:

                print("\nInvalid choice. Please try again.")


# ---------------------------------
# Main
# ---------------------------------

if __name__ == "__main__":

    studio = TaskPriorityStudio()

    studio.menu()