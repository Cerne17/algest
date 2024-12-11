from tree import BinaryTreeNode as TreeNode
from tree import list_tree

def traverse_preorder(root: TreeNode) -> str:
    if root is None:
        return ''
    return f'{root.value}{traverse_preorder(root.left)}{traverse_preorder(root.right)}'

def traverse_inorder(root: TreeNode) -> str:
    if root is None:
        return ''
    return f'{traverse_inorder(root.left)}{root.value}{traverse_inorder(root.right)}'

def traverse_postorder(root: TreeNode) -> str:
    if root is None:
        return ''
    return f'{traverse_postorder(root.left)}{traverse_postorder(root.right)}{root.value}'

if __name__ == '__main__':
    print(f'Preorder Reading: {traverse_preorder(list_tree)}')
    print(f'Inorder Reading: {traverse_inorder(list_tree)}')
    print(f'Postorder Reading: {traverse_postorder(list_tree)}')