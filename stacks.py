from pythonds.basic.stack import Stack

# Reverse characters in a string using a list as a stack
def reverseString(string):
    result = []
    characters = list(string)

    while len(characters) > 0:
        endVal = characters.pop()
        result.append(endVal)
    return ''.join(result)

# Reverse characters in a string using built-in stack
def reverseStringWithStack(string):
    stack = Stack()
    characters = list(string)
    result = ''

    for char in characters:
        stack.push(char)
    while not stack.isEmpty():
        result += stack.pop()
    return result

# Determine if parantheses are balanced - (
def checkParens(string):
    stack = Stack()
    isBalanced = True
    index = 0

    while index < len(string) and isBalanced:
        currentSymbol = string[index]
        index += 1
        if currentSymbol == '(':
            stack.push(currentSymbol)
        elif currentSymbol == ')':
            if stack.isEmpty():
                isBalanced = False
            else:
             stack.pop()

    if stack.isEmpty() and isBalanced:
        isBalanced = True
    else:
        isBalanced = False

    return isBalanced

openParens = '([{'
closeParens = ')]}'

def checkMatch(open, close):
    matches = openParens.index(open) == closeParens.index(close)
    return matches

# Determine if parantheses are balanced - ({[
def checkAllParens(string):
    stack = Stack()
    isBalanced = True
    index = 0

    while index < len(string) and isBalanced:
        currentSymbol = string[index]
        index += 1

        if currentSymbol in openParens:
            stack.push(currentSymbol)
        elif currentSymbol in closeParens:

            if stack.isEmpty():
                isBalanced = False
            else:
                lastOpenSymbol = stack.pop()
                if checkMatch(lastOpenSymbol, currentSymbol):
                    isBalanced = True
                else:
                    isBalanced = False
    return isBalanced

def baseConverter(number, base):
    digits = "0123456789ABCDEF"
    stack = Stack()
    result = ''

    while number > 0:
        remainder = number % base
        stack.push(remainder)
        number = number // base
        print(number)
    while not stack.isEmpty():
        num = stack.pop()
        result = result + digits[num]
    return result

result = baseConverter(26, 26)
print(result)
