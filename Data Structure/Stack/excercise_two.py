'''
    QUESTION 2.

    Write a function in python that checks if paranthesis in the string are balanced or not.
    Possible parantheses are "{}',"()" or "[]"
'''
from main import Stack


def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    return match_dict[ch1] == ch2


def is_balanced(string):
    stack = Stack()

    for char in string:
        if char == '(' or char == '[' or char == '{':
            stack.push(char)
        if char == ')' or char == ']' or char == '}':
            if stack.size() == 0:
                return False

            if not is_match(char, stack.pop()):
                return False

    return stack.size() == 0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
