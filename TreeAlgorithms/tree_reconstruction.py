from tree import BinaryTreeNode as TreeNode
from tree import list_tree 
from tree_readings import traverse_preorder, traverse_inorder, traverse_postorder

preorder: str = traverse_preorder(list_tree)
inorder: str = traverse_inorder(list_tree)
postorder: str = traverse_postorder(list_tree)

def build_tree_pre_in(preorder: str|list[str|None], inorder: str|list[str|None]) -> TreeNode: 
    if not preorder or not inorder:
        return None
    root: TreeNode = TreeNode(preorder[0])
    mid: int = inorder.index(preorder[0])
    root.left = build_tree_pre_in(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree_pre_in(preorder[mid+1:], inorder[mid+1:])
    return root

def build_tree_in_post(inorder: str|list[str|None], postorder: str|list[str|None]) -> TreeNode:
    if type(inorder) is str:
        inorder = [x for x in inorder]
    if type(postorder) is str:
        postorder = [x for x in postorder]
    inorderIndex = {value: index for index, value in enumerate(inorder)}

    def helper(l,r):
        if l>r:
            return None

        root: TreeNode = TreeNode(postorder.pop())
        mid: int = inorder.index(root.value)
        root.right = helper(mid+1, r)
        root.left = helper(l, mid-1)
        return root
    return helper(0, len(inorder)-1)

if __name__ == '__main__':
    tree: TreeNode = build_tree_pre_in(preorder, inorder)
    print('PREORDER AND INORDER RECONSTRUCTION')
    print('Original Tree:')
    print(list_tree)
    print('Reconstructed Tree:')
    print(tree)
    print(f'Are they the same: \n -Preorder: {preorder == traverse_preorder(tree)}')
    print(f' -Inorder: {inorder == traverse_inorder(tree)}')

    print('\n\nINORDER AND POSTORDER RECONSTRUCTION')
    tree2: TreeNode = build_tree_in_post(inorder, postorder)
    print('Original Tree')
    print(list_tree)
    print('Reconstructed Tree')
    print(tree2)
    print(f'Are they the same: \n -Inorder: {inorder == traverse_inorder(tree2)}')
    print(f' -Postorder: {postorder == traverse_postorder(tree2)}')
