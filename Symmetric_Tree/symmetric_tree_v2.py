from binary_tree import TreeNode, create_tree

def is_tree_symmetric(root: TreeNode | None) -> bool:
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    
    stack = [(root.left, root.right)]

    while stack:
        t1, t2 = stack.pop()

        if not t1 and not t2:
            continue

        if not t1 or not t2 or t1.val != t2.val:
            return False
        
        stack.append((t1.left, t2.right))
        stack.append((t1.right, t2.left))
    
    return True

print(is_tree_symmetric(create_tree([1,2,2,3,4,4,3])))
print(is_tree_symmetric(create_tree([1,2,2,None,3,None,3])))