from tree import BinaryTreeNode
import numpy as np
class OptimalBst:
    def __init__(self, freq: list[int], freq_prime=list[int], tree_name: str='Optimal BST') -> None:
        self.freq = freq
        self.freq_prime = freq_prime
        self.frequency_matrix = [[0 for i in range(len(freq))] for j in range(len(freq))]
        self.cost_matrix = [[0 for i in range(len(freq))] for j in range(len(freq))]
        self.k_matrix = [[0 for i in range(len(freq))] for j in range(len(freq))]
        self.matrix_size = len(freq)
        self.tree = None
        self.tree_name = tree_name

    def __str__(self) -> str:
        if self.tree is None:
            self.compute_optimal_bst()
        return f'Frequency Matrix:\n{np.array(self.frequency_matrix)}\nCost Matrix:\n{np.array(self.cost_matrix)}\nK Matrix:\n{np.array(self.k_matrix)}\n{self.tree.print_tree(self.tree_name)}'



    def _calculate_frequency_sums(self, i: int, j: int) -> int:
        '''
        Receives as input the i,j coordinates of a frequency matrix element
        Computes the summations and returns the integer result
        i: lower coordinate/boundary
        j: higher coordinate/boundary
        summation: sum(i<k<=j) freq + sum(i<=k<=j) freq_prime
        '''
        freq_partial: int = 0
        freq_prime_partial: int = 0

        for k in range(i+1,j+1): # Goes from i+1 to j
            freq_partial += self.freq[k]

        for k in range(i, k+1): # Goes from i to j
            freq_prime_partial += self.freq_prime[k]

        return freq_partial + freq_prime_partial

    def _compute_best_combination(self, i:int, j:int) -> tuple[int]:
        '''
        Receives as inputs:
            - j,i: coordinates of the element
        delta is the absolute value of the difference between j and i,
        it is the total amount of combinations that can be made.
        '''
        best_combination, combination_value = 0, 0
        delta:int = abs(j-i)
        x_vector = []
        y_vector = []
        combinations: list[int] = [0 for i in range(delta)]

        for k in range(j-delta,j):
            x_vector.append(self.cost_matrix[i][k])
        for k in range(i+1, i+delta+1):
            y_vector.append(self.cost_matrix[k][j])

        combinations = [x_vector[k]+y_vector[k] for k in range(len(x_vector))]
        
        combination_value = min(combinations)
        best_combination = combinations.index(combination_value)+1

        return (best_combination, combination_value)
    
    def _compute_frequency_matrix(self) -> None:
        if len(self.freq) != len(self.freq_prime):
            print('Invalid Frequency Vectors: Size does not match!')
            return

        # Diagonal
        for i in range(self.matrix_size):
            self.frequency_matrix[i][i] = self.freq_prime[i]

        # Other coordinates
        for j in range(self.matrix_size):
            for i in range(j+1, self.matrix_size):
                self.frequency_matrix[j][i] = self._calculate_frequency_sums(j,i)

    def _compute_cost_and_k_matrices(self) -> None:
        # Diagonal
        for i in range(self.matrix_size):
            # cost matrix
            self.cost_matrix[i][i] = 0
            # k matrix
            self.k_matrix[i][i] = None

        # Second Diagonal
        for i in range(0,self.matrix_size-1):
            # cost matrix
            self.cost_matrix[i][i+1] = self.frequency_matrix[i][i+1]
            # k matrix
            self.k_matrix[i][i+1] = i+1

        # Other Diagonals
        for k in range(2,self.matrix_size):
            for i in range(self.matrix_size-k):
                best_combination, combination_value = self._compute_best_combination(i,i+k)
                # cost matrix
                self.cost_matrix[i][i+k] = combination_value+self.frequency_matrix[i][i+k]
                # k matrix
                self.k_matrix[i][i+k] = best_combination + i

    def _generate_tree(self, i, j) -> None:
        if self.k_matrix[i][j] is None:
            return None
        current_value = self.k_matrix[i][j]
        return BinaryTreeNode(current_value, 
            self._generate_tree(i,current_value-1),
            self._generate_tree(current_value,j)
        )

    def compute_optimal_bst(self) -> BinaryTreeNode:
        self._compute_frequency_matrix()
        self._compute_cost_and_k_matrices()
        self.tree = self._generate_tree(0, self.matrix_size-1)
        return self.tree


exercicio4a = OptimalBst(
    [0,10,1,3,2],
    [2,1,1,1,1],
    tree_name='Exercicio 4a'
)
print(exercicio4a)
exercicio4b = OptimalBst(
    [0,5,4,7,8,3,0],
    [6,0,3,8,7,4,5],
    tree_name='Exercicio 4b'
)
print(exercicio4b)
exercicio4c = OptimalBst(
    [0,1,1,1,1,1],
    [1,1,1,1,1,1],
    tree_name='Exercicio 4c'
)
print(exercicio4c)
exercicio4d = OptimalBst(
    [0,7,9,12,2,7,3,10,2,1],
    [8,2,4,6,7,9,1,3,5,0],
    tree_name='Exercicio 4d'
)
print(exercicio4d)
exercicio4e = OptimalBst(
    [0,10,9,8,7,6,5,4,3,2,1],
    [0,0,0,0,0,0,0,0,0,0,0],
    tree_name='Exercicio 4e'
)
print(exercicio4e)