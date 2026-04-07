from max_heap import MaxHeap
from task import Task

heap = MaxHeap()
order_counter = 0

def add_task():
    global order_counter
    name = input("Enter task name: ")
    priority = int(input("Enter task priority (1-10): "))
    task = Task(name, priority,order_counter)
    order_counter += 1
    heap.insert(task)

def get_next_task():
    task = heap.extract_max()
    if task:
        print(f"Next task: {task}")
    else:
        print("No tasks available.")

heap.insert(Task("Task 1", 5))
heap.insert(Task("Task 2", 8))
heap.insert(Task("Task 3", 3))
add_task()
get_next_task()
get_next_task()