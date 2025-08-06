from collections import deque

from binary_tree import TreeNode, create_tree


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    queue = deque([(p, q)])

    while queue:
        node_p, node_q = queue.popleft()

        if not node_p and not node_q:
            continue

        if not node_p or not node_q or node_p.val != node_q.val:
            return False
        
        queue.append([node_p.left, node_q.left])
        queue.append([node_p.right, node_q.right])

    return True

list1 = [1]
list2 = [1, None, 3]

tree1 = create_tree(list1)
tree2 = create_tree(list2)

print(is_same_tree(tree1, tree2))
