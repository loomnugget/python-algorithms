# Array - mutable, all the same type
# Pros: element access is quick
# Cons: insert/delete element is slow (have to shift/unshift)
import array as arr
import numpy as np

test_array = arr.array("I", [1, 2, 3, 4])

# List - mutable, different types , built into python
list = [1, 2, 3]
list.append(4)
list.remove(1)
list.sort()

array2 = np.array([1, 2, 3, 4])
new_array = array2/3

ones = np.ones((2,2))
zeros = np.zeros((2,2), dtype=np.int16)
identity = np.identity(3) # creates 3x3 identity matrix

def fibonacci(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# Stack = last in, first out - use lists (real life = calculator)
stack = [1, 2, 3, 4, 5] # bottom -> top (add and remove from the top)
stack.append(6)
stack.pop()

# Queue - first in, first out
# Lists are not efficient - append/pop is not fast, insertion/deletion is also
# not fast since element positions have to shift

# Deque - can remove from front and back
# Ex: palindrome

# Linked List
# Pros: insert/delete doesn't require shifting
# Cons: finding an element requires traversal of entire list

# Hash tables
# Pros: insert/delete/direct access is quick
# Cons: need a key to find an element, can't guarantee ordered retrieval

# BST
# Pros: insert/delete, fast access, sorted order, can retrieve elements in order
# Cons: pain to set up
