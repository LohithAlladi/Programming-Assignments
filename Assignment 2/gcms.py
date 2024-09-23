from bin import Bin
from avl import AVLTree,comp_1,comp_2
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.BinTree1 = AVLTree(compare_function=comp_1)
        self.BinTree2 = AVLTree(compare_function=comp_2)
        self.ObjectTree = AVLTree(compare_function=comp_2)
        pass 

    def add_bin(self, bin_id, capacity):
        nodei = Node((capacity, bin_id))
        nodei1 = Node(Bin(bin_id, capacity))
        tree1 = self.BinTree1
        tree2 = self.BinTree2
        tree1.insert_node(self.BinTree1.root, nodei)
        tree2.insert_node(self.BinTree2.root, nodei1)
        pass
        

    def add_object(self, object_id, size, color):
        object = Object(object_id, size, color)
        d = None
        match color:
            case Color.BLUE:
                d = self.cfit_lid(self.BinTree1.root,size)
            case Color.YELLOW:
                d = self.cfit_gid(self.BinTree1.root,size)
            case Color.RED:
                d = self.lfit_lid(self.BinTree1.root,size)
            case Color.GREEN:
                d = self.lfit_gid(self.BinTree1.root,size)
        
        print(d)

        if d is None:
            raise NoBinFoundException
        else:
            object.bin = d[1]
            self.ObjectTree.insert_node(self.ObjectTree.root,Node(object))
            binf = self.BinTree2.find(d[1])

            binf.add_object(object)

            self.BinTree1.delete_node(self.BinTree1.root, Node(d))
            self.BinTree1.insert_node(self.BinTree1.root, Node((d[0]-size,d[1])))

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        ob = self.ObjectTree.find(object_id)
        self.ObjectTree.delete(self.ObjectTree.root,object_id)

        bid = ob.bin
        s = ob.size
        binf = self.BinTree2.find(bid)
        if object_id==2005:
            print(bid)
            print(self.inorderlist(binf.objects.root))
        
        
        self.BinTree1.delete_node(self.BinTree1.root, Node((binf.capacity,bid)))

        binf.capacity += s
        self.BinTree1.insert_node(self.BinTree1.root, Node((binf.capacity,bid)))

        binf.remove_object(object_id)
        
        

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        d = self.BinTree2.find(bin_id) # Write find function in avl
        size = d.capacity
        l = self.inorderlist(d.objects.root) 
        return (size,l)
        pass


    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        d = self.ObjectTree.find(object_id) # Write find function in avl
        return d.bin
        pass    

    def cfit_lid(self, root, size):
        bin_possible = None
        current = root
        while current:
            if current.data[0] == size:
                while current.left and current.data[0]==current.left.data[0]  :
                    current = current.left
                return current.data
            elif current.data[0] > size:
                # If current key is greater than the key, it is a potential choice
                bin_possible = current
                # Move to the left to check for smaller choices
                current = current.left
            else:
                # Move to the right to find a larger element
                current = current.right
        if bin_possible:
            while bin_possible.left and bin_possible.data[0]==bin_possible.left.data[0]  :
                bin_possible = bin_possible.left
        # If no exact match is found, return the best choice
        return bin_possible.data if bin_possible else None
    
    def cfit_gid(self, root, size):
        bin_possible = None
        current = root
        while current:
            if current.data[0] == size:
                while current.right and current.data[0]==current.right.data[0]  :
                    current = current.right
                return current.data
            elif current.data[0] > size:
                # If current key is greater than the key, it is a potential choice
                bin_possible = current
                # Move to the left to check for smaller choices
                current = current.left
            else:
                # Move to the right to find a larger element
                current = current.right
        while bin_possible.right and bin_possible.data[0]==bin_possible.right.data[0]  :
            bin_possible = bin_possible.right
        # If no exact match is found, return the best choice
        return bin_possible.data if bin_possible else None
        
    def lfit_lid(self, root, size):
        prev = None
        current = root
        bin_possible = current

        while current.right:
            prev = current
            current = current.right
            if prev.data[0]!=current.data[0]:
                bin_possible = current

        while bin_possible.left and bin_possible.data[0]==bin_possible.left.data[0]:
            bin_possible = bin_possible.left

        return bin_possible.data if (bin_possible and bin_possible.data[0]>=size ) else None

    def lfit_gid(self, root, size):
        current = root 
        while current.right != None:
            current = current.right
        return current.data if current.data[0] >= size else None
        
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
    
    def inorderlist(self,root):
        if root is None:
            return list()
        return self.inorderlist(root.left) + [root.data.id] + self.inorderlist(root.right)
        
        

            
        