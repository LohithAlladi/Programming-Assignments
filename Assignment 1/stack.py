class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.list = []
        pass
    # Verified
    def push(self, p):
        self.list.append(p)
    # Verified
    def pop(self):
        if (self.is_empty()):
            return 
        return self.list.pop()
    # Verified
    def top(self):
        return self.list[-1]
    # Verified 
    def length(self):
        return int(len(self.list))
    # Verified
    def is_empty(self):
        if (self.length() != 0):
            return False
        return True
        
    # You can implement this class however you like

    
    