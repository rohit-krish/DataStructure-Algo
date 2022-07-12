from main import Stack

'''
    QUESTION 1.

    Write a function in python that can reverse a string using stack data structure.
'''

def reverse_string(string: str):
    stack = Stack()
    count = 0
    while count != len(string):
        stack.push(string[count])
        count += 1

    count = 0
    res_string = ''
    while count != len(string):
        res_string += stack.pop()
        count += 1

    return res_string


print(reverse_string('rohit'))
