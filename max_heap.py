class MaxHeap:
    def __init__(self):
        self.heap = []

    def _is_higher_priority(self, t1, t2):
        if t1.priority != t2.priority:
            return t1.priority > t2.priority
        return t1.order < t2.order

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self._is_higher_priority(self.heap[index], self.heap[parent]):
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                break

    def extract_max(self):
        if not self.heap:
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
            highest = index

            if left < size and self._is_higher_priority(self.heap[left], self.heap[highest]):
                highest = left

            if right < size and self._is_higher_priority(self.heap[right], self.heap[highest]):
                highest = right

            if highest != index:
                self.heap[index], self.heap[highest] = (
                    self.heap[highest],
                    self.heap[index],
                )
                index = highest
            else:
                break

    def peek(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return not self.heap

    def get_all_tasks(self):
        return list(self.heap)

    def __str__(self):
        return str(self.heap)