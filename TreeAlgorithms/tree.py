class BinaryTreeNode:
    '''
    Implements a Binary Tree Node
    '''
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        lines = self._get_vertical_lines()
        return "\n".join(line.rstrip() for line in lines)

    def _get_vertical_lines(self):
        lines, _, _, _ = self._display_aux(self)
        return lines

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = f"{node.value}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = f"{node.value}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = f"{node.value}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = f"{node.value}"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def max_depth(self) -> int:
        if not self:
            return 0
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def print_tree(self, title: str) -> None:
        max_depth = self.max_depth()
        # Calculate the width based on the maximum depth and the length of the longest line
        max_line_length = max_depth * 4 + len("Value: 100 | Left: 100 | Right: 100")
        width = max(max_line_length, 50)  # Ensure a minimum width of 50 characters
        header_footer = '+' + '-' * width + '+'
        title_line = f'|{title:^{width}}|'
        
        print(header_footer)
        print(title_line)
        print(header_footer)
        
        stack = [(self, 0)]  # Stack to hold nodes and their level
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
        '''
        Search for the target value in the BST, if found returns the path to that target node
        '''
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
        '''
        Search for the target value in the BST, if not found insert the target value
        Returns the path to the target node, and a boolean value indicating if the target 
        value was found or inserted
        '''
        path, found = self.find_value(target)
        if not found:
            # Insert the value and return the path
            parent_node: BinaryTreeNode = self._navigate_path(path[:-1])
            if path[-1] == 'L':
                parent_node.left = BinaryTreeNode(target)
            else:
                parent_node.right = BinaryTreeNode(target)
        return path, not found

    def remove_value(self, target: int|str) -> bool:
        '''
        Searches the target value in the BST, if found removes the target node
        Returns True if the target node is removed, False otherwise
        '''
        path, found = self.find_value(target)
        if not found:
            return False
        parent_node: BinaryTreeNode = self._navigate_path(path[:-1])
        if parent_node.value > target:
            parent_node.left = None
        else:
            parent_node.right = None
        return True

    def preorder_traverse(self):
        if self is None:
            return ''
        if self.left is None and self.right is None:
            return f'{self.value}'
        if self.left is None:
            return f'({self.value}{self.right.preorder_traverse()})'
        if self.right is None:
            return f'({self.value}{self.left.preorder_traverse()})'
        else:
            return f'({self.value}{self.left.preorder_traverse()}{self.right.preorder_traverse()})'

class GenericTreeNode:
    def __init__(self, value: str|int, children: list[BinaryTreeNode|None]=[]) -> None:
        self.value = value
        self.children = children

class AvlTreeNode (BinaryTreeNode):
    def __init__(self, value: str|int, left=None, right=None, height=1) -> None:
        super().__init__(value, left, right)
        self.height = height

full_tree: BinaryTreeNode = BinaryTreeNode('A',
    BinaryTreeNode('B',
        BinaryTreeNode('D'),
        BinaryTreeNode('E')
    ),
    BinaryTreeNode('C',
        BinaryTreeNode('F'),
        BinaryTreeNode('G')
    )    
)

deep_tree: BinaryTreeNode = BinaryTreeNode('A',
    BinaryTreeNode('B',
        BinaryTreeNode('D',
            BinaryTreeNode('H'),
            BinaryTreeNode('I')),
        BinaryTreeNode('E',
            BinaryTreeNode('J'),
            BinaryTreeNode('L'))
    ),
    BinaryTreeNode('C',
        BinaryTreeNode('F',
            BinaryTreeNode('M'),
            BinaryTreeNode('N')),
        BinaryTreeNode('G',
            BinaryTreeNode('O'),
            BinaryTreeNode('P'))
    )    
)

list_tree: BinaryTreeNode = BinaryTreeNode('A',
    BinaryTreeNode('B',
        BinaryTreeNode('D',
            BinaryTreeNode('H')
        ),
        BinaryTreeNode('E',
            BinaryTreeNode('I',
                BinaryTreeNode('M',
                    right=BinaryTreeNode('O')
                )
            )
        )
    ),
    BinaryTreeNode('C',
        BinaryTreeNode('F',
            BinaryTreeNode('J')
        ),
        BinaryTreeNode('G',
            right=BinaryTreeNode('L',
                right=BinaryTreeNode('N',
                    BinaryTreeNode('P')
                )
            )
        )
    )
)

right_tree: BinaryTreeNode = BinaryTreeNode('A',
    BinaryTreeNode('B'),
    BinaryTreeNode('C',
        BinaryTreeNode('F'),
        BinaryTreeNode('G')
    )    
)

left_tree: BinaryTreeNode = BinaryTreeNode('A',
    BinaryTreeNode('B',
        BinaryTreeNode('D'),
        BinaryTreeNode('E')
    ),
    BinaryTreeNode('C')    
)

generic_tree: GenericTreeNode = GenericTreeNode(1,
    [
        GenericTreeNode(7,
            [
                GenericTreeNode(5),
                GenericTreeNode(4, [GenericTreeNode(10)])
            ]
        ),
        GenericTreeNode(3,
            [GenericTreeNode(9,
                [
                    GenericTreeNode(2),
                    GenericTreeNode(8),
                    GenericTreeNode(6)
                ]
            )]
        )
    ]
)

if __name__ == "__main__":
    print(right_tree)
    print(list_tree)