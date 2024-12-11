from tree import GenericTreeNode, generic_tree 

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def max_depth(self) -> int:
        if not self:
            return 0
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def print_tree(self, title: str) -> None:
        max_depth = self.max_depth()
        max_line_length = max_depth * 4 + len("Value: 100 | Left: 100 | Right: 100")
        width = max(max_line_length, 50)
        header_footer = '+' + '-' * width + '+'
        title_line = f'|{title:^{width}}|'
        
        print(header_footer)
        print(title_line)
        print(header_footer)
        
        stack = [(self, 0)]
        while stack:
            node, level = stack.pop()
            if node:
                indent = ' ' * (level * 4)
                line = f'{indent}Value: {node.value:^6} | Left: {node.left.value if node.left else "None":^6} | Right: {node.right.value if node.right else "None":^6}'
                print(f'|{line:<{width}}|')
                if node.right:
                    stack.append((node.right, level + 1))
                if node.left:
                    stack.append((node.left, level + 1))
        
        print(header_footer)

    def _navigate_path(self, path: str) -> 'BinaryTreeNode':
        current_node: BinaryTreeNode = self
        for direction in path:
            if direction == 'L':
                current_node = current_node.left
            elif direction == 'R':
                current_node = current_node.right
        return current_node

    def find_value(self, target: int|str) -> tuple[str, bool]:
        path: str = ''
        current_node: BinaryTreeNode = self

        while current_node is not None:
            if current_node.value == target:
                return path, True
            if current_node.value > target:
                path += 'L'
                current_node = current_node.left
            else:
                path += 'R'
                current_node = current_node.right
        return path, False
        
    def insert_value(self, target: int|str) -> tuple[str, bool]:
        path, found = self.find_value(target)
        if not found:
            parent_node: BinaryTreeNode = self._navigate_path(path[:-1])
            if path[-1] == 'L':
                parent_node.left = BinaryTreeNode(target)
            else:
                parent_node.right = BinaryTreeNode(target)
        return path, not found

    def remove_value(self, target: int|str) -> bool:
        path, found = self.find_value(target)
        if not found:
            return False
        parent_node: BinaryTreeNode = self._navigate_path(path[:-1])
        if parent_node.value > target:
            parent_node.left = None
        else:
            parent_node.right = None
        return True

class AvlTreeNode(BinaryTreeNode):
    def __init__(self, value: str|int, left=None, right=None, height=0) -> None:
        super().__init__(value, left, right)
        self.height = height

    def update_height(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = max(left_height, right_height) + 1

def is_avl_tree(node: AvlTreeNode) -> bool:
    if node is None:
        return True

    left_height = node.left.height if node.left else -1
    right_height = node.right.height if node.right else -1

    if abs(left_height - right_height) > 1:
        return False

    return is_avl_tree(node.left) and is_avl_tree(node.right)

def lcrsconversion(generic_tree: GenericTreeNode) -> AvlTreeNode: #Binary Tree
    '''
    Implements the Left-Child Right-Sibling algorithm.
    '''
    if generic_tree is None:
        return None
    binary_tree: AvlTreeNode = AvlTreeNode(generic_tree.value)

    if generic_tree.children:
        binary_tree.left = lcrsconversion(generic_tree.children[0])

    current_node: AvlTreeNode = binary_tree.left
    for child in generic_tree.children[1:]:
        current_node.right = lcrsconversion(child)
        current_node = current_node.right
    
    return binary_tree

generic_tree: GenericTreeNode = GenericTreeNode(1,
    [
        GenericTreeNode(7,
            [
                GenericTreeNode(5),
                GenericTreeNode(4,
                    [GenericTreeNode(10)]
                )
            ]
        ),
        GenericTreeNode(3,
            [
                GenericTreeNode(9,
                    [
                        GenericTreeNode(2),
                        GenericTreeNode(8),
                        GenericTreeNode(6)
                    ]
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    binary_tree: AvlTreeNode = lcrsconversion(generic_tree)
    binary_tree.print_tree('Binary Tree')
    print(f'Is the tree AVL? {is_avl_tree(binary_tree)}')
