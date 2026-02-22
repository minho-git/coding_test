 # class Node:
#
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class Tree:
#
#     def __init__(self, value):
#         self.root = Node(value)
#
# tree = Tree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
#
# def dfs(node: Node):
#     # 전위 순회
#     if node is not None:
#         print(node.value)
#
#     if node.left is not None:
#         dfs(node.left)
#
#     # 중위 순회
#     # if node is not None:
#     #     print(node.value)
#
#     if node.right is not None:
#         dfs(node.right)
#
#     # 후위 순회
#     # if node is not None:
#     #     print(node.value)
#
# dfs(tree.root)

def dfs(v):
    if v > 7:
        return

    print(v, end=" ")
    dfs(v * 2)
    # print(v, end=" ")
    dfs(v * 2 + 1)
    # print(v, end=" ")
    # 병합정렬은 후위순회?? 나중에 푼다.
    


dfs(1)
