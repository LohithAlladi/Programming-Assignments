from node import Node

def comp_1(node_1, node_2):
    if node_1.data[0] < node_2.data[0]:
        return -1
    elif node_1.data[0] > node_2.data[0]:
        return 1 
    else:
        if node_1.data[1]> node_2.data[1]:
            return 1 
        elif node_1.data[1] < node_2.data[1]:
            return -1
        else:
            return 0

def comp_2(node_1, node_2):
    if node_1.data.id > node_2.data.id:
        return 1 
    elif node_1.data.id < node_2.data.id:
        return -1
    else:
        return 0


def height(node):
        if node is None:
            return 0
        else:
            return node.height

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    
    # right rotate subtree rooted with y
    def right_rotate(self , y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(height(y.left), height(y.right))
        x.height = 1 + max(height(x.left), height(x.right))

        # Return new root
        return x

    # left rotate subtree rooted with x
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(height(x.left), height(x.right))
        y.height = 1 + max(height(y.left), height(y.right))

        # Return new root
        return y

    # Get balance factor of node 
    def get_balance(self,node):
        if not node:
            return 0
        return height(node.left) - height(node.right)

    # Recursive function to insert a key in
    # the subtree rooted with node
    def insert_node(self, node , nodei, s = True):

        if self.size == 0:
            self.root = nodei
            self.size += 1
            return 
        
        if s:
            self.size += 1
        
        if not node:
            return nodei

        if self.comparator(nodei, node) == -1 :
            node.left = self.insert_node(node.left, nodei, False)
            
        elif self.comparator(nodei, node)== 1:
            node.right = self.insert_node(node.right, nodei, False)

        # Update height of this ancestor node
        node.height = 1 + max(height(node.left), height(node.right)) 
        

        # Get the balance factor of this ancestor node
        balance = self.get_balance(node)

        # If this node becomes unbalanced, 
        # then there are 4 cases

        # Left Left Case
        if balance > 1 and self.comparator(nodei, node.left) == -1:
            if node == self.root:
                self.root = node.left
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and self.comparator(nodei, node.right)== 1:
            if node == self.root:
                self.root = node.right
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and self.comparator(nodei, node.left)== 1:
            if node == self.root:
                self.root = node.left.right
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and self.comparator(nodei, node.right) == -1:
            if node == self.root:
                self.root = node.right.left
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # Return the (unchanged) node pointer
        return node
    
    def min_value_node(self,node):
        current = node

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current   
 
    def delete_node(self, root, key, s=True ):
        
        if s:
            self.size -= 1

        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, then it lies in left subtree
        if self.comparator(key,root) == -1:
            root.left = self.delete_node(root.left, key,False)

        # If the key to be deleted is greater than the root's key, then it lies in right subtree
        elif self.comparator(key,root) == 1:
            root.right = self.delete_node(root.right, key, False)

        # if key is same as root's key, then this is the node to be deleted
        
        else:
            # node with only one child or no child
            if root.left is None or root.right is None:
                temp = root.left if root.left else root.right

                # No child case
                if temp is None:
                    root = None
                    if s:
                        self.root = None
                else:  # One child case
                    root = temp

            else:
                # node with two children: Get the inorder successor (smallest in the right subtree)
                temp = self.min_value_node(root.right)

                # Copy the inorder successor's 
                # data to this node
                root.data = temp.data

                # Delete the inorder successor
                root.right = self.delete_node(root.right, temp,False)
            # # H-Code
            # if root.left is None:
            #     return root.right
            # if root.right is None:
            #     return root.left
            
            # temp_node = self.min_value_node(root.right)
            # root.data = temp_node.data
            # root.right = self.delete_node(root.right,key,False)   
            # H-Code
        # If the tree had only one node then return
        if root is None:
            return root

        # STEP 2: UPDATE HEIGHT OF THE CURRENT NODE
        root.height = max(height(root.left), 
                        height(root.right)) + 1

        # STEP 3: GET THE BALANCE FACTOR OF THIS 
        # NODE (to check whether this node 
        # became unbalanced)
        balance = self.get_balance(root)

        # If this node becomes unbalanced, then 
        # there are 4 cases

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            if root == self.root:
                self.root = root.left
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            if root == self.root:
                self.root = root.right
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left)<0:
            if root == self.root:
                self.root = root.left.right
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) >0:
            if root == self.root:
                self.root = root.right.left
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key, s=True):

        if s:
            self.size -= 1

        # STEP 1: PERFORM STANDARD BST DELETE
        if root is None:
            return root

        # If the key to be deleted is smaller 
        # than the root's key, then it lies in 
        # left subtree
        if key < root.data.id:
            root.left = self.delete(root.left, key, False)

        # If the key to be deleted is greater 
        # than the root's key, then it lies in 
        # right subtree
        elif key > root.data.id:
            root.right = self.delete(root.right, key, False)

        # if key is same as root's key, then 
        # this is the node to be deleted
        else:
            # node with only one child or no child
            if root.left is None or root.right is None:
                temp = root.left if root.left else root.right

                # No child case
                if temp is None:
                    root = None
                    if s:
                        self.root = None
                        return
                else:  # One child case
                    root = temp

            else:
                if self.size == 0:
                    self.root = None
                # node with two children: Get the 
                # inorder successor (smallest in 
                # the right subtree)
                temp = self.min_value_node(root.right)

                # Copy the inorder successor's 
                # data to this node
                root.data = temp.data

                # Delete the inorder successor
                root.right = self.delete(root.right, temp.data.id,False)
        
        # If the tree had only one node then return
        if root is None:
            return root

        # STEP 2: UPDATE HEIGHT OF THE CURRENT NODE
        root.height = max(height(root.left), 
                        height(root.right)) + 1

        # STEP 3: GET THE BALANCE FACTOR OF THIS NODE (to check whether this node became unbalanced)
        balance = self.get_balance(root)

        # If this node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            if root == self.root:
                self.root = root.left
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            if root == self.root:
                self.root = root.left.right
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            if root == self.root:
                self.root = root.right
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            if root == self.root:
                self.root = root.right.left
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def find(self,key):
        current = self.root
        while current:
            if current.data.id > key:
                current = current.left
            elif current.data.id < key:
                current = current.right
            else:
                return current.data