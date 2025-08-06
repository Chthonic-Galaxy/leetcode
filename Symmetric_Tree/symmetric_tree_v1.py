from binary_tree import TreeNode, create_tree

def is_tree_symmetric(root: TreeNode | None) -> bool:
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    

    def is_mirror(t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        
        if not t1 or not t2 or t1.val != t2.val:
            return False
        
        return (is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))

    return is_mirror(root.left, root.right)

print(is_tree_symmetric(create_tree([1,2,2,3,4,4,3])))
print(is_tree_symmetric(create_tree([1,2,2,None,3,None,3])))
