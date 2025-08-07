from binary_tree import TreeNode, create_tree

def binary_tree_maximum_depth(root: TreeNode | None):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    
    stack = [(root, 1)]
    md = 0

    while stack:
        node, depth = stack.pop()

        if node:
            md = max(md, depth)

            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
        
    return md
    
if __name__ == "__main__":
    print(binary_tree_maximum_depth(create_tree([3,9,20,None,None,15,7])))
    print(binary_tree_maximum_depth(create_tree([1, None, 2])))
