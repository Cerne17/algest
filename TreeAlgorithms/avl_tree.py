from tree import BinaryTreeNode
from rotations import *

class AvlTreeNode (BinaryTreeNode):
    def __init__(self, value: str|int, left=None, right=None) -> None:
        super().__init__(value, left, right)
        self.height = 1
    
    def update_height(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = max(left_height, right_height) + 1

    def get_balance(self) -> int:
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height


# Custom Rotations are needed for this code to work properly
def rightRotate(A):
    B = A.left
    A.left = B.right
    B.right = A
    A.update_height()
    B.update_height()
    return B

def leftRotate(A):
    B = A.right
    A.right = B.left
    B.left = A
    A.update_height()
    B.update_height()
    return B

def leftRightRotate(C):
    C.left = leftRotate(C.left)
    return rightRotate(C)

def rightLeftRotate(B):
    B.right = rightRotate(B.right)
    return leftRotate(B)

def balance_node(node: AvlTreeNode) -> AvlTreeNode:
    balance = node.get_balance()

    if balance > 1:
        if node.left.get_balance() >= 0:
            print(f'Right rotation at {node.value} (balance: {balance})')
            print(f'Node left\'s child height: {node.left.height if node.left else 0} (balance: {node.left.get_balance() if node.left else 0})')
            print(f'Node right\'s child height: {node.right.height if node.right else 0} (balance: {node.right.get_balance() if node.right else 0})')
            print(root)
            return rightRotate(node)
        else:
            print(f'Left-Right rotation at {node.value} (balance: {balance})')
            print(f'Node left\'s child height: {node.left.height if node.left else 0} (balance: {node.left.get_balance() if node.left else 0})')
            print(f'Node right\'s child height: {node.right.height if node.right else 0} (balance: {node.right.get_balance() if node.right else 0})')
            print(root)
            return leftRightRotate(node)
    if balance < -1:
        if node.right.get_balance() <= 0:
            print(f'Left rotation at {node.value} (balance: {balance})')
            print(f'Node left\'s child height: {node.left.height if node.left else 0} (balance: {node.left.get_balance() if node.left else 0})')
            print(f'Node right\'s child height: {node.right.height if node.right else 0} (balance: {node.right.get_balance() if node.right else 0})')
            print(root)
            return leftRotate(node)
        else:
            print(f'Right-Left rotation at {node.value} (balance: {balance})')
            print(f'Node left\'s child height: {node.left.height if node.left else 0} (balance: {node.left.get_balance() if node.left else 0})')
            print(f'Node right\'s child height: {node.right.height if node.right else 0} (balance: {node.right.get_balance() if node.right else 0})')
            print(root)
            return rightLeftRotate(node)
    return node

def transformToAvl(root: AvlTreeNode) -> AvlTreeNode:
    if root is None:
        return None
    
    root.left = transformToAvl(root.left)
    root.right = transformToAvl(root.right)

    root.update_height()
    return balance_node(root)

if __name__ == "__main__":
    root = AvlTreeNode(100,
        AvlTreeNode(50,
            AvlTreeNode(25,
                AvlTreeNode(10,
                    AvlTreeNode(5,
                        AvlTreeNode(2,
                            AvlTreeNode(1)
                        )
                    )
                )
            )
        )
    )
    print('Unbalanced Tree')
    print(root)
    root = transformToAvl(root)
    print('Avl Tree')
    print(root)