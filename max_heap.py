# max heap that supports the functions: insert(task) and extract_max()
class MaxHeap:
    def __init__(self):
        self.heap = [] # creates the heap
    
    def insert(self,task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0] # the first element will be the largest
        self.heap[0] = self.heap.pop() # replace first element with the last element to prevent a "hole"
        self._heapify_down(0) # sort the swapped element so that its in the correct place
        return root # return the largest element

    def _heapify_up(self,index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self,index):
        size = len(self.heap)

        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[index],self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
        