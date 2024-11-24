'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import*
from heap import*
from treasure import*

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
        self.crewmates = [CrewMate() for _ in range(m)]
        self.crewmate_heap = Heap(self.compare_crewmates, self.crewmates)
        # Write your code here
        pass
    
    def compare_crewmates(self, c1, c2):
        return c1.load < c2.load
    
    def compare_treasures(self, t1, t2):
        return t1[0]< t2[0] if t1[0] != t2[0] else t1[1].id < t2[1].id


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
        current_crewmate = self.crewmate_heap.extract()
        current_crewmate.treasures_list.append(treasure)
        current_crewmate.load = max(current_crewmate.load,treasure.arrival_time)+treasure.size
        self.crewmate_heap.insert(current_crewmate)
    
    def print_treasures(self):
        '''
        Prints the treasures assigned to each crewmate.
        '''
        for idx, crewmate in enumerate(self.crewmates):
            print(f"Crewmate {idx + 1}:")
            for treasure in crewmate.treasures_list:
                print(f"  Treasure {treasure.id}, Arrival Time: {treasure.arrival_time}, Size: {treasure.size}")


    
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
        completed_treasures = []

        for crewmate in self.crewmates:

            if crewmate.treasures_list:

                processing_queue = Heap(self.compare_treasures, [])
                current_time = 0
                next_arrival_time = 0

                crewmate.set_treasures()

                i = 0
                
                while i< len(crewmate.treasures_list)-1:

                    process = crewmate.treasures_list[i]
                    priority = process.size + process.arrival_time
                    current_time=crewmate.treasures_list[i].arrival_time
                    next_arrival_time = crewmate.treasures_list[i+1].arrival_time
                    processing_queue.insert((priority,process))

                    while current_time<next_arrival_time:
                        if len(processing_queue.init_array)==0:
                            break
                        treasure = processing_queue.extract()[1]
                        if treasure.remaining_size <= next_arrival_time - current_time:
                            current_time += treasure.remaining_size
                            treasure.completion_time = current_time
                            completed_treasures.append(treasure)
                        else:
                            treasure.remaining_size -= next_arrival_time - current_time
                            processing_queue.insert((treasure.remaining_size + treasure.arrival_time,treasure))
                            current_time = next_arrival_time
                    i+=1

                process = crewmate.treasures_list[i]
                priority = process.remaining_size + process.arrival_time
                current_time=crewmate.treasures_list[i].arrival_time
                processing_queue.insert((priority,process))

                while processing_queue.init_array:
                    treasure = processing_queue.extract()[1]
                    current_time += treasure.remaining_size
                    treasure.completion_time = current_time
                    completed_treasures.append(treasure)

        completed_treasures.sort(key=lambda t: t.id)
        return completed_treasures
    


