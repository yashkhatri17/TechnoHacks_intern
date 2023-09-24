class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            return "No tasks in the to-do list."
        else:
            task_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(self.tasks)])
            return f"To-Do List:\n{task_list}"

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] += " (Completed)"
            return f"Task {task_index} marked as completed."
        else:
            return "Invalid task index."

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            return f"Task {task_index} deleted."
        else:
            return "Invalid task index."

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added to the to-do list.")
        elif choice == '2':
            print(todo_list.view_tasks())
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            print(todo_list.mark_completed(task_index))
        elif choice == '4':
            task_index = int(input("Enter the task index to delete: "))
            print(todo_list.delete_task(task_index))
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()












class ToDoLiast :
  
   def __init__(self) :
       self.tasks = []
    
   def Add_Task(self,task) :
       self.tasks.append(task)
   
   def Veiw_Task(self) :
       if not self.tasks:
           return "not in the task"
       else:
           task_list = "/n".join([f"{i+1}.{task}" for i,task in enumerate(self.tasks)])
           return  f"To-Do List:\n{task_list}"
       
   def Mark_complete(self,task_index) :
       if 1< task_index < len(self.tasks) :
          self.tasks[task_index-1]+= "complete"
          return f"Task {task_index} marked as completed."
       else:
           return  "Invalid task index."
       
   def Delet_Task(self,task_index) :
       if 1<task_index<len(self.tasks):
           del self.tasks[task_index - 1]
           return f"Task {task_index} deleted."
       else:
           return "Invalid task index."
       
def Main():
    todo_list = ToDoList()

    while True:
         print("\nTo-Do List Menu:")
         print("1. Add Task")
         print("2. View Tasks")
         print("3. Mark Task as Completed")
         print("4. Delete Task")
         print("5. Quit")

         choice = input("Enter your choice (1/2/3/4/5): ")

         
         if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added to the to-do list.")
         elif choice == '2':
            print(todo_list.view_tasks())
         elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            print(todo_list.mark_completed(task_index))
         elif choice == '4':
            task_index = int(input("Enter the task index to delete: "))
            print(todo_list.delete_task(task_index))
         elif choice == '5':
            print("Goodbye!")
            break
         else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()