#-*- coding: utf-8 -*-
class Node():
    """Tree Node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

''' Build tree like this.
    ----
    ` a `
    `-- `
      |
     / \
    /   \_
  ----    \
  ` b `    ----
  `---`    ` c `
   |       `---`
    \        | \__
     ----    ----  ----
     ` d `   ` e ` ` f `
     `---`   `---` `---`

'''
def build_tree():
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.right = Node('d')
    root.right.left = Node('e')
    root.right.right = Node('f')
    return root

root = build_tree()
assert root.value == 'a'
assert root.left.value == 'b'
assert root.left.right.value == 'd'
assert root.right.value == 'c'
assert root.right.left.value == 'e'
assert root.right.right.value == 'f'

