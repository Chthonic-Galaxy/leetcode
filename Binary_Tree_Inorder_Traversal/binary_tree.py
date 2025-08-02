from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(l: list):
    root = TreeNode(l[0])
    queue = deque([root])

    i = 1
    while queue and i < len(l):
        parent = queue.popleft()

        if i < len(l):
            left_val = l[i]
            i += 1
            if left_val is not None:
                parent.left = TreeNode(left_val)
                queue.append(parent.left)

        if i < len(l):
            right_val = l[i]
            i += 1
            if right_val is not None:
                parent.right = TreeNode(right_val)
                queue.append(parent.right)
        
    return root

if __name__ == "__main__":
    list1 = [1, None, 2, 3]
    list2 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, None, None, 9]

    tree1 = create_tree(list1)
    tree2 = create_tree(list2)

    print(f"Корень дерева 1: {tree1.val}")
    print(f"Левый ребенок корня 1: {tree1.left}")
    print(f"Правый ребенок корня 1: {tree1.right.val}")
    print(f"Левый ребенок узла 2: {tree1.right.left.val}")
    print(f"Правый ребенок узла 2: {tree1.right.right}")
