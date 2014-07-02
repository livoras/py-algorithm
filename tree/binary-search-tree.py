# Binary Search Tree is of greate effecience of dynamicly  
# searching. The best case is O(log(n)) (Balant Tree).
# The worst case is O(n) (Tree degenerates to a link list.)

class Node():
    def __init__(self, value=None, parent=None):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

    def is_left(self):
        return self.parent and self.parent.left == self

    def is_right(self):
        return self.parent and self.parent.right == self

class Binary_search_tree():
    def __init__(self):
        self.root = None

    def find(self, value):
        current_node = self.root
        while current_node:
            if current_node.value == value:
                return current_node
            elif current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def find_min(self, node=None):
        node = node or self.root
        while node and node.left:
            node = node.left
        return node

    def find_max(self, node=None):
        node = node or self.root
        while node and node.right:
            node = node.right
        return node

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            node = self.root
            while True:
                if value < node.value:
                    if not node.left:
                        node.left = Node(value, node)
                        return node.left
                    else:
                        node = node.left
                else:
                    if not node.right:
                        node.right = Node(value, node)
                        return node.right
                    else:
                        node = node.right

    def delete(self, value):
        node = self.find(value)
        if not node:
            raise KeyError("Value %s is not found." % value)

        if node.left and node.right: # has both children.
            successor = self.find_min(node.right)
            self.delete(successor.value)
            self.replace_node(node, successor)
            successor.left = node.left
            successor.right = node.right

        elif node.left: # has a left or right child
            self.replace_node(node, node.left)
        elif node.right:
            self.replace_node(node, node.right)

        else:
            self.replace_node(node, None)

        return node    

    def replace_node(self, node, new_node):
        if node.is_left():
            node.parent.left = new_node
        elif node.is_right():
            node.parent.right = new_node
        else:
            self.root = new_node
        if new_node:
            new_node.parent = node.parent


        
# ------------------- tests ----------------------
traversals = __import__("tree-traversals")

bst = Binary_search_tree()
for i in [5, 30, 2, 40, 25, 4]:
    bst.insert(i)

def test_bst_insert():
    result = []
    def fn(node):
        result.append(node.value)
    traversals.inorder(bst.root, fn)
    assert result == [2, 4, 5, 25, 30, 40]
    print 'OK: Insertion passed.'

def test_find_min():
    min_node = bst.find_min()
    assert min_node.value == 2
    print "OK: Finding minimal value passed."

def test_find_max():
    max_node = bst.find_max()
    assert max_node.value == 40
    print "OK: Finding maximal value passed."

def test_find():
    node = bst.find(25)
    assert node.value == 25
    print "OK: Finding specify value passed."

def build_a_bst():
    bst = Binary_search_tree()
    for i in [5, 30, 2, 40, 25, 4, 1, 10, 42, 26, 36]:
        bst.insert(i)
    return bst

def test_delete():
    bst = build_a_bst()
    bst.delete(1)
    assert bst.root.left.left == None
    assert inorder(bst) == [2, 4, 5, 10, 25, 26, 30, 36, 40, 42]
    bst.delete(30)
    assert bst.root.right.value == 36
    assert inorder(bst) == [2, 4, 5, 10, 25, 26, 36, 40, 42]
    bst.delete(2)
    assert bst.root.left.value == 4
    assert inorder(bst) == [4, 5, 10, 25, 26, 36, 40, 42]
    bst.delete(5)
    assert bst.root.value == 10
    assert inorder(bst) == [4, 10, 25, 26, 36, 40, 42]
    bst.insert(37)
    assert inorder(bst) == [4, 10, 25, 26, 36, 37, 40, 42]
    print "OK: Deletion passed."

def inorder(bst):
    result = []
    def fn(node):
        result.append(node.value)
    traversals.inorder(bst.root, fn)
    return result


if __name__ == "__main__":
    test_bst_insert()
    test_find_min()
    test_find_max()
    test_find()
    test_delete()
