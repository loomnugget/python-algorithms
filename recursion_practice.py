# Find the sum of a list of numbers
def calculateSum(list):
    if list:
        val1 = list.pop()
        val2 = calculateSum(list)
        if val2:
            sum = val1 + val2
            return sum
        else:
            return val1

# Implementation 2
def calculateSum2(list):
    if len(list) == 1:
        return list[0]
    else:
        # list[1:] - returns list with item 0 removed
        return list[0] + calculateSum2(list[1:])

# Factorial - n * n-1 * n-2, factorial of 0 = 1
def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1)

def reverseString(string):
    if len(string) == 1:
        return string
    else:
        # newString = string.split('')
        newString = string[:-1]
        print(newString)
        reverseString(newString)

        return newString

result = reverseString('claudia')
# print(result)
