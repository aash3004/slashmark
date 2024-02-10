class Task:
    def __init__(self, description, priority=0):
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority=0):
        task = Task(description, priority)
        self.tasks.append(task)

    def remove_task(self, index):
        del self.tasks[index]

    def list_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task.description} - Priority: {task.priority}")

    def prioritize_task(self, index, priority):
        self.tasks[index].priority = priority

    def recommend_task(self, description):
        recommended_task = None
        max_similarity = -1

        for task in self.tasks:
            similarity = self._calculate_similarity(description, task.description)
            if similarity > max_similarity:
                recommended_task = task
                max_similarity = similarity

        return recommended_task

    def _calculate_similarity(self, desc1, desc2):
        words1 = set(desc1.lower().split())
        words2 = set(desc2.lower().split())
        intersection = words1.intersection(words2)
        return len(intersection) / (len(words1) + len(words2) - len(intersection))

def print_menu():
    print("""
    Task Manager Menu:
    -------------------
    1. Add Task
    2. Remove Task
    3. List Tasks
    4. Prioritize Task
    5. Get Task Recommendation
    6. Exit
    """)

def main():
    task_manager = TaskManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAdd Task")
            print("--------")
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (default is 0): "))
            task_manager.add_task(description, priority)
            print("Task added successfully!")
        elif choice == '2':
            print("\nRemove Task")
            print("-----------")
            task_manager.list_tasks()
            if task_manager.tasks:
                index = int(input("Enter task index to remove: ")) - 1
                if 0 <= index < len(task_manager.tasks):
                    task_manager.remove_task(index)
                    print("Task removed successfully!")
                else:
                    print("Invalid task index.")
        elif choice == '3':
            print("\nList Tasks")
            print("----------")
            task_manager.list_tasks()
        elif choice == '4':
            print("\nPrioritize Task")
            print("---------------")
            task_manager.list_tasks()
            if task_manager.tasks:
                index = int(input("Enter task index to prioritize: ")) - 1
                if 0 <= index < len(task_manager.tasks):
                    priority = int(input("Enter new priority: "))
                    task_manager.prioritize_task(index, priority)
                    print("Task prioritized successfully!")
                else:
                    print("Invalid task index.")
        elif choice == '5':
            print("\nGet Task Recommendation")
            print("------------------------")
            description = input("Enter task description to get recommendation: ")
            recommended_task = task_manager.recommend_task(description)
            if recommended_task:
                print(f"Recommended Task: {recommended_task.description}")
            else:
                print("No recommendation found.")
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
