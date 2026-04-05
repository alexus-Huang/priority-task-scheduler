from max_heap import MaxHeap
from task import Task

heap = MaxHeap()
t1 = Task(priority=10, name="Fix Bug")
t2 = Task(priority=1,name="Do HW")
print("Inserting tasks...")
heap.insert(t1)
heap.insert(t2)



print(heap.extract_max())