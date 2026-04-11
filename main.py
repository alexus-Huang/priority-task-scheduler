from max_heap import MaxHeap
from task import Task

heap = MaxHeap()
order_counter = 0

def add_task():
    global order_counter
    name = input("Enter task name: ")
    priority = int(input("Enter task priority (1-10): "))
    task = Task(name, priority, order_counter)
    order_counter += 1
    heap.insert(task)

def get_next_task():
    task = heap.peek()
    if task:
        print(f"Next task: {task}")
    else:
        print("No tasks available.")



def view_all_tasks():
    if heap.is_empty():
        print("No tasks available.")
    else:
        print("All tasks:")
        for task in heap.get_all_tasks():
            print(task)
def complete_task():
    task = heap.extract_max()
    if task:
        print(f"Completed task: {task}")
    else:
        print("No tasks to complete.")

def remove_task():
    name = input("Enter task name to remove: ")
    for i in range(len(heap)):
        if heap.heap[i].name == name:
            heap.heap[i] = heap.heap[-1]
            heap.heap.pop()
            heap._heapify_down(i)
            print(f"Removed task: {name}")
            return
    
def reminder_queue():
    if heap.is_empty():
        print("No tasks to do!")
    else:
        for tasks in heap.get_all_tasks():
            print(tasks)

heap.insert(Task("Task 1", 5,1))
heap.insert(Task("Task 2", 8,2))
heap.insert(Task("Task 3", 3,3))
add_task()
complete_task()
get_next_task()
get_next_task()
print("Reminder queue")
reminder_queue()