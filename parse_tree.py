from pythonds.basic.stack import Stack
from btree import BinaryTree
import operator

def buildParseTree(expression):
    list = expression.split()
    parentStack = Stack()
    tree = BinaryTree('')
    parentStack.push(tree)
    currentTree = tree

    for i in list:
        # if opening parens, this is the starting point,
        # add a new left child and set current tree to that node
        # parent is still the initial tree
        if i == '(':
            currentTree.insertLeft('')
            parentStack.push(currentTree)
            leftNode = currentTree.getLeftChild()
            currentTree = leftNode

        # if the current symbol is a number, set the current node
        # to the number and return to the parent node
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootValue(int(i))
            parent = parentStack.pop()
            currentTree = parent
        # if the current symbol is an operand, this assumes you
        # are back at the parent node, so set the root value, create
        # a new right node and go to it
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootValue(i)
            currentTree.insertRight('')
            parentStack.push(currentTree)
            rightNode = currentTree.getRightChild()
            currentTree = rightNode

        # If closing parens, go back to the parent of the current node
        elif i == ')':
            currentParent = parentStack.pop()
            currentTree = currentParent
        else:
            raise ValueError

    return tree

def evaluate(parseTree):
    operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    # fn(val1, val2)
    leftNode = parseTree.getLeftChild()
    rightNode = parseTree.getRightChild()

    if leftNode and rightNode:
        operand = parseTree.getRootValue()
        fn = operators[operand]
        return fn(evaluate(leftNode), evaluate(rightNode))
    else:
        return parseTree.getRootValue()


testTree = buildParseTree('( 3 + ( 4 * 5 ) )')
result = evaluate(testTree)
