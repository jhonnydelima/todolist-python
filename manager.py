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
  return

def update_task_name(tasks, task_index, new_task_name):
  tasks[task_index]["task"] = new_task_name
  print(f'\nTask {task_index + 1} updated to "{new_task_name}".')
  return

def complete_task(tasks, task_index):
  tasks[task_index]["completed"] = True
  print(f'\nTask "{tasks[task_index]["task"]}" marked as completed.')
  return

def delete_completed_tasks(tasks):
  for task in tasks:
    if task["completed"]:
      tasks.remove(task)
  print("\nCompleted tasks deleted.")
  return

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
  elif option == "3":
    show_tasks(tasks)
    task_index = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_index < len(tasks):
      new_task_name = input("Enter the new task name: ")
    else:
      print("\nInvalid task.")
      continue
    update_task_name(tasks, task_index, new_task_name)
  elif option == "4":
    show_tasks(tasks)
    task_index = int(input("Enter the task number to complete: ")) - 1
    if 0 <= task_index < len(tasks):
      complete_task(tasks, task_index)
    else:
      print("\nInvalid task.")
      continue
  elif option == "5":
    delete_completed_tasks(tasks)
    show_tasks(tasks)
  elif option == "6":
    break
  else:
    print("\nInvalid option.")