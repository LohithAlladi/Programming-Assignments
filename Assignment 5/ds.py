class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0  # Pointer to the front of the queue

    def enqueue(self, item):
        # Add item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove item from the front of the queue
        if self.is_empty():
            raise IndexError("Empty Queue")
        item = self.queue[self.front]
        self.front += 1
        # Cleanup unused space
        if self.front > len(self.queue) // 2:
            self.queue = self.queue[self.front:]
            self.front = 0
        return item

    def is_empty(self):
        # Check if queue is empty
        return self.front == len(self.queue)

    def size(self):
        # Return the size of the queue
        return len(self.queue) - self.front
    
class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        self.comparator = comparison_function
        self.init_array = init_array[:]
        # Write your code here
        pass
        
    def insert(self, value):
        # Write your code here
        
        (self.init_array).append(value)

        # self.upheap(len(self.init_array)-1)

        n = len(self.init_array)-1
        while n != 0:
            k = (n-1)//2
            if self.comparator(self.init_array[n], self.init_array[k]):
                self.init_array[k], self.init_array[n] = self.init_array[n], self.init_array[k]
                n = k
            else:
                break

    
    def extract(self):
        # Write your code here
        A = self.init_array

        if len(A) == 0:
            return None
        
        if len(A) == 1:
            return A.pop()
        
        A[0], A[-1] = A[-1], A[0]
        k  = A.pop()
        n = len(A)
        i = 0 
        while(2*i+2 <= n):

            small = i
            left = 2*i+1
            right = 2*i+2

            if left < n and self.comparator(A[left], A[small]):
                small = left

            if right < n and self.comparator(A[right], A[small]):
                small = right

            if small != i:
                A[small], A[i] = A[i], A[small]
                i = small

            else:
                break 

        return k
    
        pass
    
    def top(self):
        # Write your code here
        return self.init_array[0] if self.init_array else None
        
    # You can add more functions if you want to
    def clear(self):
        self.init_array = []

    def heapify(self):
        A = self.init_array
        n = len(A)
        i = 0
        while(2*i+2 <= n):

            small = i
            left = 2*i+1
            right = 2*i+2

            if left < n and self.comparator(A[left], A[small]):
                small = left

            if right < n and self.comparator(A[right], A[small]):
                small = right

            if small != i:
                A[small], A[i] = A[i], A[small]
                i = small

            else:
                break

# Wait  
class HashMap:
    def __init__(self,table_size):
        self.table_size = table_size
        self.table = [[[] for _ in range(100)] for _ in range(self.table_size)]

    def insert(self,x):
        flight, arrival_time = x[0]
        slot = self.table[flight.flight_no]
        i = arrival_time % 100
        slot[i].append((arrival_time,x[1]))

    def find(self,x):
        flight, arrival_time = x
        slot = self.table[flight.flight_no]
        i = arrival_time % 100
        place = slot[i]
        for key in place:
            if key[0] == arrival_time:
                return key[1]
        