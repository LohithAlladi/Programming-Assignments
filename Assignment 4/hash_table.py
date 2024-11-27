from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type = collision_type
        self.size = 0
        if collision_type == "Chain":
            self.table_size = params[1]  # Initial size
            self.z = params[0]  # For polynomial hash
            self.table = [[] for _ in range(self.table_size)]
        else:  # Linear or Double
            if collision_type == "Linear":
                self.table_size = params[1]
                self.z = params[0]
            if collision_type == "Double":
                self.z = params[0]
                self.z2 = params[1]  # For second hash function
                self.c2 = params[2]  # For compression in second hash
                self.table_size = params[3]
            self.table = [None] * self.table_size
        pass
    
    def c_ord(self,x):
        if x.isupper() :
            return ord(x)-39
        if x.islower():
            return ord(x)-97
        if x.isdigit():
            return int(x)
        

    def _poly_hash(self, key):
        """Polynomial accumulation hash function"""
        if isinstance(key, tuple):  # For HashMap
            key = key[0]
        Key = key[::-1]
        hash_val = 0
        for char in str(Key):
            hash_val = (hash_val * self.z + self.c_ord(char)) % self.table_size
        return hash_val % self.table_size

    def _double_hash(self, key):
        """Second hash function for double hashing"""
        if isinstance(key, tuple):  # For HashMap
            key = key[0]
        Key = key[::-1]
        hash_val = 0
        for char in str(Key):
            hash_val = (hash_val * self.z2 + self.c_ord(char)) % self.c2
        hash_val = (self.c2 - hash_val % self.c2) # % self.c2
        return hash_val
    
    def get_slot(self, key):
        if isinstance(key, tuple):  # For HashMap
            key = key[0]

        hash_val = 0
        for char in str(key):
            hash_val = (hash_val * self.z + self.c_ord(char)) 
        return hash_val % self.table_size
        
    def get_load(self):
        return (self.size / self.table_size)
        
    
    def __str__(self):
        if self.collision_type == "Chain":
            # Handle chaining case
            formatted_slots = []
            for slot in self.table:
                if not slot:  # Empty slot
                    formatted_slots.append("⟨EMPTY⟩")
                else:
                    # Format each element in the chain and join with semicolons
                    elements = [self._format_element(elem) for elem in slot]
                    formatted_slots.append(" ;".join(elements))
            string = " | ".join(formatted_slots)
            return string 
        else:
            # Handle linear probing and double hashing cases
            formatted_slots = []
            for element in self.table:
                formatted_slots.append(self._format_element(element))
            return " | ".join(formatted_slots)

    def _format_element(self, element):
        """Helper method to format individual elements"""
        if element is None:
            return "⟨EMPTY⟩"
        if isinstance(element, tuple):
            # For HashMap entries
            return f"({element[0]}, {element[1]})"
        # For HashSet entries
        return str(element)
    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self, next_table_size):

        self.table_size = next_table_size
        # Change table size
        old_table = self.table # Copy the old table

        if self.collision_type == "Chain":
            self.table  = [[] for _ in range(self.table_size)]
            for slot in old_table:
                for x in slot:
                    self.insert(x)
        else:
            self.table = [None] * self.table_size
            for x in old_table:
                if x is not None:
                    self.insert(x)
        
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, key):
        if not self.find(key):
            if self.collision_type == "Chain":
                slot = super()._poly_hash(key)
                if key not in self.table[slot]:
                    self.table[slot].append(key)
                    self.size += 1
            else:
                initial_pos = super()._poly_hash(key)
                if self.table[initial_pos] == None:
                        self.table[initial_pos] = key
                        self.size += 1
                else:
                    jump = 1
                    if self.collision_type == "Double": 
                        jump = super()._double_hash(key)
                        if jump == 0:
                            jump = 1 
                    pos = (initial_pos + jump) % self.table_size 
                    while self.table[pos] != None and pos != initial_pos:
                        pos = (pos + jump) % self.table_size
                    if pos != initial_pos:
                        self.table[pos] = key
                        self.size += 1

    def find(self, key):
        if self.collision_type == "Chain":
            slot = super()._poly_hash(key)
            for item in self.table[slot]:
                    if item == key:
                        return True 
            return False
        else:
            initial_pos = super()._poly_hash(key)
            if self.table[initial_pos] == key:
                return True
            else:
                jump = 1
                if self.collision_type == "Double": 
                    jump = super()._double_hash(key)
                    if jump == 0:
                        jump = 1 
                pos = (initial_pos + jump) % self.table_size
                while key != self.table[pos] and pos != initial_pos:
                    pos = (pos + jump) % self.table_size
                if key == self.table[pos]:
                    return True
                return False
    
    def get_slot(self, key):
        return super().get_slot(key)
    
    def get_load(self):
        return super().get_load()
    
    def __str__(self):
        return super().__str__()

    def rehash(self, next_table_size):

        self.table_size = next_table_size
        # Change table size
        old_table = self.table # Copy the old table

        if self.collision_type == "Chain":
            self.table  = [[] for _ in range(self.table_size)]
            for slot in old_table:
                for x in slot:
                    self.insert(x)
        else:
            self.table = [None] * self.table_size
            for x in old_table:
                if x is not None:
                    self.insert(x)

class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, x):
        # x = (key, value)
        key = x[0]
        if self.collision_type == "Chain":
                slot = super()._poly_hash(key)
                i = 0
                for item in (self.table[slot]):
                    if item[0] == key:
                        self.table[slot][i] = x  # Update value
                        return
                    i+=1
                self.table[slot].append(x)
                self.size += 1
        else:
            initial_pos = super()._poly_hash(key)
            if self.table[initial_pos] == None :
                    self.table[initial_pos] = x
                    self.size += 1
            elif self.table[initial_pos][0] == key:
                self.table[initial_pos] = x
            else:
                jump = 1
                if self.collision_type == "Double": 
                    jump = super()._double_hash(key)
                    if jump == 0:
                        jump = 1 
                pos = (initial_pos + jump) % self.table_size 
                while self.table[pos] != None and self.table[pos][0] != key and pos != initial_pos:
                    pos = (pos + jump) % self.table_size
                if pos != initial_pos:
                    if self.table[pos] == None:
                        self.size += 1
                    self.table[pos] = x 
    
    def find(self, key):
        if self.collision_type == "Chain":
            slot = super()._poly_hash(key)
            for item in (self.table[slot]):
                    if item[0] == key:
                        return item[1] 
            return None
        else:
            initial_pos = super()._poly_hash(key)
            if self.table[initial_pos][0] == key:
                return self.table[initial_pos][1]
            else:
                jump = 1
                if self.collision_type == "Double": 
                    jump = super()._double_hash(key)
                    if jump == 0:
                        jump = 1 
                pos = (initial_pos + jump) % self.table_size
                while key != self.table[pos][0] and pos != initial_pos:
                    pos = (pos + jump) % self.table_size
                if key == self.table[pos][0]:
                    return self.table[pos][1]
                return None
    
    def rehash(self, next_table_size):

        self.table_size = next_table_size
        # Change table size
        old_table = self.table # Copy the old table

        if self.collision_type == "Chain":
            self.table  = [[] for _ in range(self.table_size)]
            for slot in old_table:
                for x in slot:
                    self.insert(x)
        else:
            self.table = [None] * self.table_size
            for x in old_table:
                if x is not None:
                    self.insert(x)

    def get_slot(self, key):
        return super().get_slot(key)
    
    def get_load(self):
        return super().get_load()
    
    def __str__(self):
        return super().__str__()