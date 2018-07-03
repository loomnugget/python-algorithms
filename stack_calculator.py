from pythonds.basic.stack import Stack

def formatExpression(expression):
    precedenceValues = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    operands = Stack()
    postFixes = []
    list = expression.split()

    for item in list:
        if item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or item in "0123456789":
            postFixes.append(item)
        else:
            operands.push(item)
        return precedenceValues

print(formatExpression("A * B + C * D"))
