# Create a binaryTree
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # If there is no left child, add a new tree at the left node
    # if there is a left child, push it down further on the tree
    # by adding a new tree to the left node and setting the current tree
    # to it's left child
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            newTree = BinaryTree(newNode)
            # Insert the new tree at the current left node
            # and set the new tree's left child to the displaced tree
            newTree.leftChild = self.leftChild
            self.leftChild = newTree

    def insertRight(self, newNode):
            if self.rightChild == None:
                self.rightChild = BinaryTree(newNode)
            else:
                newTree = BinaryTree(newNode)
                newTree.rightChild = self.rightChild
                self.rightChild = newTree

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self, object):
        self.key = object

    def getRootValue(self):
        return self.key

# Test building a tree
def testBuildTree():
    tree = BinaryTree('a')

    # Create left side
    tree.insertLeft('b')
    leftNode = tree.getLeftChild()
    leftNode.insertRight('d')

    # Create right side
    tree.insertRight('c')
    rightNode = tree.getRightChild()
    rightNode.insertLeft('e')
    rightNode.insertRight('f')

    # Display values - a b c d e f
    print(tree.getRootValue())
    print(tree.getLeftChild().getRootValue())
    print(tree.getRightChild().getRootValue())
    print(leftNode.getRightChild().getRootValue())
    print(rightNode.getLeftChild().getRootValue())
    print(rightNode.getRightChild().getRootValue())

# testBuildTree()
