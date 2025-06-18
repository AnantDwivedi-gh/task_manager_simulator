from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nOptions: add <task> <priority>, complete, show, done, undo, exit")
        command = input("Command: ").strip()

        if command.startswith("add"):
            try:
                _, task, priority = command.split(maxsplit=2)
                manager.add_task(task, int(priority))
            except:
                print("Usage: add <task_name> <priority>")
        elif command == "complete":
            manager.complete_task()
        elif command == "show":
            manager.show_tasks()
        elif command == "done":
            manager.show_completed()
        elif command == "undo":
            manager.undo()
        elif command == "exit":
            print("Exiting Task Manager...")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
