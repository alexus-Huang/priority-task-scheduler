class MaxHeap:
    def __init__(self):
        self.heap = []

    def _is_higher_priority(self, t1, t2):
        if t1.priority > t2.priority:
            return True
        if t1.priority == t2.priority:
            return t1.order < t2.order
        
        return False

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self._is_higher_priority(self.heap[index], self.heap[parent]):
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def extract_max(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self._is_higher_priority(self.heap[left], self.heap[largest]):
                largest = left

            if right < size and self._is_higher_priority(self.heap[right], self.heap[largest]):
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break
        
    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False
    
    def get_all_tasks(self):
        return self.heap

    def __str__(self):
        return str(self.heap)