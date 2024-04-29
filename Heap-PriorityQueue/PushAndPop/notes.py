# Min Heap
class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self,val):
        self.heap.append(val)
        i = len(self.heap) - 1

        #  Percolate up
        while i > 1 and self.heap[i] < self.heap[i// 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
