'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        
        # Write your code here
        self.crew_array = Heap()
        self.non_empty = []
        
        for i in range(m):
            c = CrewMate()
            self.crew_array.insert(((0,0),c))
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        
        c = self.crew_array.extract()
        c[1].treasure.append(treasure)
        c[1].load = max(c[0][0]+treasure.size,treasure.arrival_time+treasure.size)
        self.crew_array.insert(((c[1].load,0),c[1]))
        if c[1].occupied is False:
            self.non_empty.append(c[1])
            c[1].occupied = True
        
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        
        lis = []
        
        for c in self.non_empty:
            
            for i in range(len(c.treasure)):
                c.treasure[i].res()
            current_t = 0
            pq = Heap()
            for i in range(len(c.treasure)):
                treasure_arr = c.treasure[i]
                current_t = treasure_arr.arrival_time
                pq.insert(((-treasure_arr.priority,treasure_arr.id),treasure_arr))
                if i< len(c.treasure)-1:
                    nex = c.treasure[i+1].arrival_time
                    while current_t < nex:
                        for j in range(pq.size()):
                            pq.heap[j][1].wait += nex - current_t
                        if pq.size()==0:
                            break
                        process = pq.extract()[1]
                        if current_t + process.remaining <= nex:
                            current_t += process.remaining
                            process.completion_time = current_t
                            lis.append(process)
                            process.remaining_size = 0
                        else:
                            process.remaining -= nex- current_t
                            process.priority = process.wait - process.remaining
                            pq.insert(((-process.priority,process.id),process))
                            current_t = nex
                else:
                    while pq.size()>0:
                        process = pq.extract()[1]
                        current_t += process.remaining
                        process.completion_time = current_t
                        lis.append(process)
                        process.remaining = 0
                        
        lis.sort(key = lambda treasure: treasure.id)
        return lis
    
    # You can add more methods if required
    def print_stored_treasures(self):
        '''
        Prints the treasures stored by each crewmate
        '''
        print("\nStored Treasures by CrewMates:")
        for crewmat in self.crew_array.heap:
            crewmat = crewmat[1]
            print(f"CrewMate Load = {crewmat.load}, Treasures = {[treasur.id for treasur in crewmat.treasure]}")