def show_menu():
    print("What do you want to do")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
def main():
    tasks =[]
 
    while True :
      show_menu()
      choice = input("Enter the choice(1,2,3,4):").strip()
      if choice=="1" :
         task = input("Enter tasks: ")
         tasks.append(task)
         print(f"Task added: {task}")
      elif choice == "2":
         if not tasks:
            print("there are no tasks")
         else:
            print("Your Tasks")
            for i,task in enumerate(tasks,1):
               print(f"{i}. {task}") 
      elif choice == "3":
         if not tasks :
            print ("No tasks to remove")
         else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                   removed = tasks.pop(task_num)
                   print(f"{removed}")
                else:
                   print("Enter valid value ")
            except ValueError:
                    print("❌ Please enter a number.")
      elif choice == "4":
            print("👋 Exiting To-Do List. See you next time!")
            break
      else :
          print ("Enter value between 1-4")
main()