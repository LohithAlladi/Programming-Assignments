from avl import AVLTree, comp_2
from node import Node

class Bin:
    def __init__(self, bin_id, capacity):
        self.objects = AVLTree(comp_2)
        self.id = bin_id
        self.capacity = capacity

    def add_object(self, object):
        # Implement logic to add an object to this bin
        nodei = Node(object)
        (self.objects).insert_node(self.objects.root, nodei)
        self.capacity -= object.size
    
    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        (self.objects).delete(self.objects.root, object_id)
        
