from tree import BinaryTreeNode as TreeNode 
from tree import full_tree, right_tree, left_tree

def rightRotate(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def leftRotate(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def leftRightRotate(C):
    C.left = leftRotate(C.left)
    return rightRotate(C)


def rightLeftRotate(B):
    B.right = rightRotate(B.right)
    return leftRotate(B)


def preorder_traverse(root):
    if root is None:
        return ''
    if root.left is None and root.right is None:
        return f'{root.value}'
    else:
        return f'({root.value}{preorder_traverse(root.left)}{preorder_traverse(root.right)})'

if __name__ == '__main__':
    # print(f'Left Skewed tree: {preorder_traverse(left_tree)}')
    # print(left_tree)
    # left_tree = rightRotate(left_tree)
    # print(f'Right Rotated tree: {preorder_traverse(left_tree)}')
    # print(left_tree)
    # expected_tree_left: TreeNode = TreeNode('B',
    #     TreeNode('D'),
    #     TreeNode('A',
    #         TreeNode('E'),
    #         TreeNode('C')
    #     )
    # )
    # print(f'Expected Tree: {preorder_traverse(expected_tree_left)}')
    # print(expected_tree_left)

    # print(f'Right Skewed Tree: {preorder_traverse(right_tree)}')
    # print(right_tree)
    # right_tree = leftRotate(right_tree)
    # print(f'Left Rotated tree: {preorder_traverse(right_tree)}')
    # print(right_tree)
    # expected_tree_right: TreeNode = TreeNode('C',
    #     TreeNode('A',
    #         TreeNode('B'),
    #         TreeNode('F')
    #     ),
    #     TreeNode('G')
    # )
    # print(f'Expected Tree: {preorder_traverse(expected_tree_right)}')
    # print(expected_tree_right)

    example_right_left: TreeNode = TreeNode('A',
        TreeNode('A_l'),
        TreeNode('C',
            TreeNode('B',
                TreeNode('B_l'),
                TreeNode('B_r'),
            ),
            TreeNode('C_r')
        )
    )
    example_left_right: TreeNode = TreeNode('C',
        TreeNode('A',
            TreeNode('A_l'),
            TreeNode('B',
                TreeNode('B_l'),
                TreeNode('B_r')
            )
        ),
        TreeNode('C_r')
    )
    print(f"Right Left Tree Before Rotation {preorder_traverse(example_right_left)}")
    print(example_right_left)
    example_right_left = rightLeftRotate(example_right_left)
    print(f"Right Left Tree After Rotation {preorder_traverse(example_right_left)}")
    print(example_right_left)
    print(f"Left Right Tree Before Rotation {preorder_traverse(example_left_right)}")
    print(example_left_right)
    example_left_right = leftRightRotate(example_left_right)
    print(f"Left Right Tree After Rotation {preorder_traverse(example_left_right)}")
    print(example_left_right)