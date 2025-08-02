from binary_tree import TreeNode, create_tree

def binary_tree_travese(root: TreeNode):
    result = []
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right
        


    return result


list1 = [1, None, 2, 3]
list2 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, None, None, 9]

tree1 = create_tree(list1)
tree2 = create_tree(list2)

print(binary_tree_travese(tree1))
print(binary_tree_travese(tree2))
