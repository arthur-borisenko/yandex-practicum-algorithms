from typing import Optional
import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value

else:
    from node import Node


def find_key(root, key):
    node = root
    parent = None
    while node:
        if key < node.value:
            parent = node
            node = node.left
        elif key == node.value:
            return parent, node
        else:
            parent = node
            node = node.right
    return None, None


def prepare_replacement_node(root):
    if root is None:
        return None, None
    node = root
    parent = None
    while node.right is not None:
        parent = node
        node = node.right
    if parent is not None:
        parent.right = node.left
    return node


def replace_node_link(parent, node, new_node):
    if parent.left is node:
        parent.left = new_node
    else:
        parent.right = new_node


def remove(root, key) -> Optional[Node]:
    if root is None:
        return None
    parent, node = find_key(root, key)
    if node is None:
        return root  # Если вершины нет в дереве, изменять его не требуется
    if root.left is None and root.right is None:  # Если дерево состояло из одной вершины, то после её удаления дерева не останется.
        return None
    right = node.right
    left = node.left
    if left is None and right is None:  # Если мы удаляем лист, то дерево останется одним деревом и не распадётся на части.
        replace_node_link(parent, node, None)
        return root
    if left is not None and right is not None:  # Если мы удаляем корень, у которого есть оба поддерева, то каждое поддерево станет отдельным деревом. Если мы удаляем вершину, у которой есть оба ребёнка и родитель, то дерево распадётся на родительское и два поддерева.
        node_to_replace = prepare_replacement_node(left)
        node_to_replace.right = right
        node_to_replace.left = left
    else:  # Только 1 ребенок - присоединяем его вместо узла
        node_to_replace = right if right is not None else left
    if parent is not None:
        replace_node_link(parent, node, node_to_replace)
    else:
        root = node_to_replace
    return root
    #  “ヽ(´▽｀)ノ”

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)




def children(node):
    c = []
    if node.left is not None:
        c.append(node.left)
    if node.right is not None:
        c.append(node.right)
    return c
def dfs(root):
    res=[]
    stack=Stack()
    node = root
    stack.push(node)
    while not stack.isEmpty():
        node = stack.pop()
        yield node.value
        for node in children(node):
            stack.push(node)
    return res

def test():
    """Data equivalent of correctness
7
1 4 2 3
2 2 4 5
3 6 6 7
4 1 -1 -1
5 3 -1 -1
6 5 -1 -1
7 7 -1 -1
1"""
    n1 = Node(value=4)
    n2 = Node(value=2)
    n3 = Node(value=6)
    n4 = Node(value=1)
    n5 = Node(value=3)
    n6 = Node(value=5)
    n7 = Node(value=7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    root = n1
    input1=list(dfs(root))
    print(*input1)
    remove(root, 1)
    output1=list(dfs(root))
    print(*output1)


if __name__ == "__main__":
    test()
