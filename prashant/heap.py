'''
Python Code to implement a heap with general comparison function
'''
def heapify(arr,n,i):
    smallest=i  
    left=2*i+1  
    right=2*i+2  
    if left<n and arr[left]<arr[smallest]:
        smallest=left
    if right<n and arr[right]<arr[smallest]:
        smallest=right
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]  
        heapify(arr,n,smallest)

def build_min_heap(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
            
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
        
        # Write your code here
        self.compare=comparison_function
        build_min_heap(init_array)
        self.view=init_array

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
        self.view.append(value)
        l=len(self.view)-1
        self.upheap(l)
    
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
        if len(self.view)==0:
            return None
        MIN=self.view[0]
        self.view[0]=self.view[-1]
        self.view.pop()
        self.downheap(0)
        return MIN
    
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
        if self.is_empty():
            return None
        return self.view[0]
    
    # You can add more functions if you want to
    def parent(self,i):
        return (i-1)//2
        
    def left(self,i):
        if 2*i+1 >= len(self.view):
            return None
        return ((2*i)+1)
        
    def right(self,i):
        if 2*i+2 >= len(self.view):
            return None
        return ((2*i)+2)
        
    def is_empty(self):
        return len(self.view)==0

    def upheap(self,i):
        while i>0 and self.compare(self.view[i],self.view[self.parent(i)]):
            self.view[self.parent(i)],self.view[i]=self.view[i],self.view[self.parent(i)]
            i=self.parent(i)
            
    def downheap(self,i):
        temp=i
        while self.right(temp)!=None:
            L=self.view[self.left(temp)]
            R=self.view[self.right(temp)]
            S=self.view[temp]
            if self.compare(L,R) and self.compare(L,S):
                self.view[self.left(temp)],self.view[temp]=self.view[temp],self.view[self.left(temp)]
                temp=2*temp+1
            elif self.compare(R,L) and self.compare(R,S):
                self.view[self.right(temp)],self.view[temp]=self.view[temp],self.view[self.right(temp)]
                temp=2*temp+2
            else:
                if ((not self.compare(L,R)) and (not self.compare(R,L))) and  self.compare(L,S):
                    self.view[self.left(temp)],self.view[temp]=self.view[temp],self.view[self.left(temp)]
                    temp=2*temp+1
                else:
                    break
        if self.left(temp)!=None:
            if self.compare(self.view[self.left(temp)],self.view[temp]):
                self.view[self.left(temp)],self.view[temp]=self.view[temp],self.view[self.left(temp)]
    