'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        self.comparator = comparison_function
        self.init_array = init_array[:]
        for i in range(len(self.init_array)-1,0,-1): self.init_array[i],self.init_array[(i-1)//2] = self.init_array[(i-1)//2],self.init_array[i] if self.comparator(self.init_array[(i-1)//2],self.init_array[i]) else self.init_array[i],self.init_array[(i-1)//2]
        # Write your code here
        pass
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
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
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
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
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        return self.init_array[0] if self.init_array else None
        
    # You can add more functions if you want to

    # def upheap(self, i):
    #     parent = (i-1)//2
    #     if i>0 and self.comparator(self.init_array[i],self.init_array[parent]):
    #         self.init_array[i],self.init_array[parent] = self.init_array[parent], self.init_array[i]
    #         self.upheap(parent)

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