'''
    Python file to implement the class CrewMate
'''
import custom
import treasure
import heap

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.treasure_list=[]
        self.treasure_heap=Heap(comp2,[])
        self.load=0
        
    
    # Add more methods if required
    def add(self,prize):
        self.treasure_list.append(prize)
        self.load=max(self.load,prize.arrival_time)+prize.size
        
    def compute_time(self):
        for j in range(len(self.treasure_list)):
            prize=self.treasure_list[j]
            prize.memory()
            t_arr=prize.arrival_time
            if self.treasure_heap.is_empty():
                self.treasure_heap.insert(prize)
            else:
                t_diff=t_arr-self.treasure_list[j-1].arrival_time
                t_corr=0
                while t_diff!=0:
                    target=self.treasure_heap.top()
                    if target==None:
                        break
                    else:
                        if t_diff<target.remaining_size:
                            target.remaining_size-=t_diff
                            t_diff=0
                        else:
                            tar=self.treasure_heap.extract()
                            tar.completion_time=self.treasure_list[j-1].arrival_time+tar.remaining_size+t_corr
                            t_corr+=tar.remaining_size
                            t_diff-=tar.remaining_size
                            tar.remaining_size=0
                self.treasure_heap.insert(prize)
                
        last_t=self.treasure_list[-1].arrival_time
        while not self.treasure_heap.is_empty():
            Top=self.treasure_heap.extract()
            Top.completion_time=last_t+Top.remaining_size
            last_t+=Top.remaining_size
            Top.remaining_size=0
            