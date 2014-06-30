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

assert infix_to_postfix('a+b*c+(d*e+f)*g') == "abc*+de*f+g*+"