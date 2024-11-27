'''
    Python file to implement the class CrewMate
'''

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
        self.load = 0 
        self.treasures_list = []
        pass
    def set_treasures(self):
        for treasure in self.treasures_list:
            treasure.set()
    # Add more methods if required