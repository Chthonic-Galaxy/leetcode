from binary_tree import TreeNode, create_tree

def binary_tree_travese_recursive(root: TreeNode):
    result = []


    def travese(node):
        if not node:
            return
        
        travese(node.left)
        result.append(node.val)
        travese(node.right)

    travese(root)
    return result


list1 = [1, None, 2, 3]
list2 = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, None, None, 9]

tree1 = create_tree(list1)
tree2 = create_tree(list2)

print(binary_tree_travese_recursive(tree1))
print(binary_tree_travese_recursive(tree2))
