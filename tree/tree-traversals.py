#-*- coding: utf-8 -*-
def preorder(node, fn):
    if node is None:
        return None
    else:
        fn(node)
        preorder(node.left, fn)
        preorder(node.right, fn)

def inorder(node, fn):
    if node is None:
        return None
    else:
        inorder(node.left, fn)
        fn(node)
        inorder(node.right, fn)

def postorder(node, fn):
    if node is None:
        return None
    else:
        postorder(node.left, fn)
        postorder(node.right, fn)
        fn(node)


bt = __import__("binary-tree")
root = bt.build_tree()

# ------------------- tests -------------------
def test_preorder():
    result = []
    def fn(node):
         result.append(node.value)
    preorder(root, fn)
    assert ''.join(result) == "abdcef"

def test_inorder():
    result = []
    def fn(node):
         result.append(node.value)
    inorder(root, fn)
    assert ''.join(result) == "bdaecf"

def test_postorder():
    result = []
    def fn(node):
         result.append(node.value)
    postorder(root, fn)
    assert ''.join(result) == "dbefca"

if __name__ == "__main__":
    test_preorder()
    test_inorder()
    test_postorder()

