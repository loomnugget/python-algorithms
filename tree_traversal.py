from btree import BinaryTree
from parse_tree import buildParseTree
import operator

def preorder(tree):
    if tree:
        print(tree.getRootValue())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


testTree = buildParseTree('( 3 + ( 4 * 5 ) )')

def postorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        print(tree.getRootValue())


def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    if tree:
        # Keep recursing through the tree until you
        # get to the bottom of the tree
        leftTree = tree.getLeftChild()
        rightTree = tree.getRightChild()

        result1 = postordereval(leftTree)
        result2 = postordereval(rightTree)

        if result1 and result2:
            function = opers[tree.getRootValue()]
            result = function(result1, result2)
            return result
        else:
            return tree.getRootValue()

def printSet(tree):
    if tree:
        leftTree = tree.getLeftChild()
        rightTree = tree.getRightChild()
        # at the bottom of the tree - result1 = 4 and result2 = 5
        result1 = printSet(leftTree)
        result2 = printSet(rightTree) # ( 4 * 5 )

        if result1 and result2:
            rootValue = tree.getRootValue()
            result = '(' + str(result1) + str(rootValue) + str(result2) + ')'
            return result
        else:
            return tree.getRootValue()




smallTree = buildParseTree('( 4 * 5 )')
largerTree = buildParseTree('( 3 + ( 4 * 5 ) )')
result = printSet(largerTree)
print(result)
