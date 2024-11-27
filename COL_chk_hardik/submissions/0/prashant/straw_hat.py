'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
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
        self.used_crew=[]
        self.crew_heap=Heap(comp3,[])
        i=0
        while i<m:
            self.crew_heap.insert(CrewMate())
            i+=1
    
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
        sel_crew=self.crew_heap.extract()
        sel_crew.add(treasure)
        self.crew_heap.insert(sel_crew)
        if sel_crew not in self.used_crew:
            self.used_crew.append(sel_crew)
    
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
        L=[]
        for crew in self.used_crew:
            crew.compute_time()
            L+=crew.treasure_list
        L1=sorted(L,key=lambda x: x.id)
        return L1
        
    
    # You can add more methods if requiredfor 