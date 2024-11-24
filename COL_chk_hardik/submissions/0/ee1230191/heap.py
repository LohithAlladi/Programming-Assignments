'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with general comparison function
    
    
    '''
    def comp1(x, y):
        return x[0] < y[0]
    
    def __init__(self, comparison_function = comp1, init_array=[]):
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
        
        # Write your code here
        
        self.comparison_function = comparison_function
        self.heap = []
        
        for item in init_array:
            self.insert(item)
        pass
    
    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2
        
    def _heapify_up(self, index):
        '''
        Rebalances the heap from index upwards
        '''
        while index > 0:
            parent_index = self._parent(index)
            if self.comparison_function(self.heap[index], self.heap[parent_index]):
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        '''
        Rebalances the heap from index downwards
        '''
        size = len(self.heap)
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            smallest = index

            if left < size and self.comparison_function(self.heap[left], self.heap[smallest]):
                smallest = left
            if right < size and self.comparison_function(self.heap[right], self.heap[smallest]):
                smallest = right
            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
        
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
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
        pass
    
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
        
        if not self.heap:
            raise IndexError("Extract from an empty heap")

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        top_value = self.heap.pop()
        if self.heap:
            self._heapify_down(0)
        return top_value
    
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
        if not self.heap:
            raise IndexError("Top from an empty heap")
        return self.heap[0]
    
    # You can add more functions if you want to
    def size(self):
        return len(self.heap)