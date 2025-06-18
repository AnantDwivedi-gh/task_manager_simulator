import heapq
from collections import deque

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.priority_queue = []
        self.completed_stack = []
        self.undo_queue = deque()
        self.task_map = {}

    def add_task(self, task, priority):
        self.tasks.append(task)
        heapq.heappush(self.priority_queue, (priority, task))
        self.task_map[task] = priority
        self.undo_queue.appendleft(("add", task))
        print(f"Added task: {task} with priority {priority}")

    def complete_task(self):
        if not self.tasks:
            print("No tasks to complete.")
            return
        _, task = heapq.heappop(self.priority_queue)
        if task in self.tasks:
            self.tasks.remove(task)
            self.completed_stack.append(task)
            self.undo_queue.appendleft(("complete", task))
            print(f"Completed task: {task}")

    def show_tasks(self):
        print("\nCurrent Tasks:")
        for task in self.tasks:
            print(f"- {task} (Priority: {self.task_map[task]})")

    def show_completed(self):
        print("\nCompleted Tasks:")
        for task in reversed(self.completed_stack):
            print(f"- {task}")

    def undo(self):
        if not self.undo_queue:
            print("Nothing to undo.")
            return
        action, task = self.undo_queue.popleft()
        if action == "add":
            self.tasks.remove(task)
            self.priority_queue = [(p, t) for p, t in self.priority_queue if t != task]
            heapq.heapify(self.priority_queue)
            del self.task_map[task]
            print(f"Undo: Removed recently added task '{task}'")
        elif action == "complete":
            self.tasks.append(task)
            priority = self.task_map[task]
            heapq.heappush(self.priority_queue, (priority, task))
            self.completed_stack.remove(task)
            print(f"Undo: Marked task '{task}' as incomplete")
