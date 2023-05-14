#Class which defines one node in the binary seacrh tree.
class Node:
    def __init__(self,d):
        self.value = d        
        self.left = None
        self.right = None

#Function to insert a node, it compares the value of the node inputted to the tree to give it the right position.
    def insert(self, d):
        if self.value:
            if d < self.value:
                if self.left is None:
                    self.left = Node(d)
                else:
                    self.left.insert(d)
            elif d > self.value:
                if self.right is None:
                    self.right = Node(d)
                else:
                    self.right.insert(d)
        else:
            self.value = d

#Function which prints the Inorder traversal.     
    def printInorder(self):
        if self.left: 
            self.left.printInorder() 
        print(self.value) 
        if self.right: 
            self.right.printInorder()
        
#Function which prints the Preorder traversal.
    def printPreorder(self):
        print(self.value)
        if self.left:
            self.left.printPreorder()
        if self.right: 
            self.right.printPreorder()

#Function which prints the Postorder traversal.
    def printPostorder(self):
        if self.left:
            self.left.printPostorder()
        if self.right:
            self.right.printPostorder()
        print(self.value)

#Initialises the root node
root = Node(27)
#Initialises other nodes
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)

#Prints the different traversal.
print("Inorder: ")
root.printInorder()
print("Preorder: ")
root.printPreorder()
print("Postorder: ")
root.printPostorder()
