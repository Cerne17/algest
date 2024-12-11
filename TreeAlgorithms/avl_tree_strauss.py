from tree import BinaryTreeNode
from rotations import *

### !TODO: FIX THIS IMPLEMENTATION : THE POINTERS ARE NOT BEING UPDATED!

class AvlTreeNode (BinaryTreeNode):
    def __init__(self, value: str|int, left=None, right=None, height=0) -> None:
        super().__init__(value, left, right)
        self.height = height

    def _define_rotation(self):
        '''
        Left Rotation:
            1. A.left.height > A.right.height
            2. A.left.left.height > A.left.right.height
        Left Right Rotation:
            1. A.left.height > A.right.height
            2. A.left.left.height < A.left.right.height
        Right Rotation:
            1. A.left.height < A.right.height
            2. A.left.left.height < A.left.right.height
        Right Left Rotation:
            1. A.left.height < A.right.height
            2. A.left.left.height > A.left.right.height
        '''
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0

        if left_height > right_height:
            left_left_height = self.left.left.height if self.left and self.left.left else 0
            left_right_height = self.left.right.height if self.left and self.left.right else 0

            if left_left_height > left_right_height:
                print(f'Right rotation at {self.value}')
                self = rightRotate(self)
            else:
                print(f'right-left rotation at {self.value}')
                self = rightLeftRotate(self)  # Left-Right rotation

        else:
            right_right_height = self.right.right.height if self.right and self.right.right else 0
            right_left_height = self.right.left.height if self.right and self.right.left else 0

            if right_right_height > right_left_height:
                print(f'left rotation at {self.value}')
                self = leftRotate(self)
            else:
                print(f'left-right rotation at {self.value}')
                self = leftRightRotate(self)  # Right-Left rotation

        return self

    def _visit(self):
        if self.left is not None:
            left_height: int = self.left.height
        else:
            left_height: int = 0 # Leaves
        if self.right is not None:
            right_height: int = self.right.height
        else:
            right_height: int = 0 # Leaves
        
        if abs(left_height - right_height) > 1:
            print(f'Imbalance detected at {self.value}')
            self = self._define_rotation()
            self._visit()
        else:
            self.height = max(left_height, right_height) + 1
            # if left_height > right_height:
            #     self.height = left_height + 1
            # else:
            #     self.height = right_height + 1


    def traverse_postorder(self) -> 'AvlTreeNode':
        if self.left is not None:
            self.left.traverse_postorder()
        if self.right is not None:
            self.right.traverse_postorder()
        self._visit()
        return self


if __name__ == '__main__':
    avl_tree = AvlTreeNode(100, 
        AvlTreeNode(50, 
            AvlTreeNode(25), 
            AvlTreeNode(75)
        ), 
        AvlTreeNode(150, 
            AvlTreeNode(125), 
            AvlTreeNode(175)
        )
    )
    avl_tree.traverse_postorder()
    avl_tree.print_tree('AVL Tree')
    avl_tree = AvlTreeNode(100, 
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
    avl_tree.print_tree('Unbalenced Tree')
    avl_tree=avl_tree.traverse_postorder()
    avl_tree.print_tree('AVL Tree')