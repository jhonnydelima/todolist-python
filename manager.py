def add_task(tasks, task_name):
  task = {"task": task_name, "completed": False}
  tasks.append(task)
  print(f'Task "{task_name}" added with success!')
  return

def show_tasks(tasks):
  if not tasks:
    print("\nNo tasks available.")
    return
  print("\nTasks:")
  for i, task in enumerate(tasks, start=1):
    status = "✓" if task["completed"] else " "
    task_name = task["task"]
    print(f"{i}. {task_name} [{status}]")

tasks = []
while True:
  print("\nMenu")
  print("1. Add a new task")
  print("2. Show tasks")
  print("3. Update task")
  print("4. Complete task")
  print("5. Delete completed tasks")
  print("6. Exit")
  option = input("Enter an option: ")
  if option == "1":
    task = input("Enter a task: ")
    add_task(tasks, task)
  elif option == "2":
    show_tasks(tasks)
  # elif option == "3":
  #   task_id = int(input("Enter the task ID: "))
  #   task = input("Enter the new task: ")
  #   update_task(task_id, task)
  # elif option == "4":
  #   task_id = int(input("Enter the task ID: "))
  #   complete_task(task_id)
  # elif option == "5":
  #   delete_completed_tasks()
  elif option == "6":
    break
  else:
    print("\nInvalid option.")