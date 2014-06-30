#-*- coding: utf-8 -*-
def infix_to_postfix(expression):
    '''
    Very good example of infix to postfix.
    '''
    result = ''
    stack = []
    for c in expression:
        if c == '(':
            stack.append(c)
        elif c in ['*', '/']:
            while len(stack) and stack[-1] in ['*', '/']:
                result = result + stack.pop()
            stack.append(c)
        elif c in ['+', '-']:
            while len(stack) and stack[-1] in ['+', '-', '*', '/']:
                result = result + stack.pop()
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                result = result + stack.pop()
            stack.pop() # pop '('
        elif c:
            result = result + c
    while len(stack):
        result = result + stack.pop()
    return result

class Node():
    """Tree Node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buile_tree_from_expression(expression):
    expression = infix_to_postfix(expression)
    stack = []
    root = None
    for c in expression:
        if c in ['+', '-', '*', '/']:
            right = stack.pop()
            left = stack.pop()
            parent = Node(c)
            parent.left = left
            parent.right = right
            stack.append(parent)
        else:
            stack.append(Node(c))
    return stack.pop()


root = buile_tree_from_expression('a+b*c+(d*e+f)*g')
assert root.value == '+'
assert root.left.value == '+'
assert root.right.value == '*'
assert root.left.left.value == 'a'
assert root.left.right.value == '*'
assert root.left.right.left.value == 'b'
assert root.left.right.right.value == 'c'
assert root.right.left.value == '+'
assert root.right.right.value == 'g'
