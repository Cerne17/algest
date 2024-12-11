# Python3 program for building Heap from Array

# To heapify a subtree rooted with node i
# which is an index in arr[]. N is size of heap

def heapify(arr, N, i):

	largest = i # Initialize largest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2

	# If left child is larger than root
	if l < N and arr[l] > arr[largest]:
		largest = l

	# If right child is larger than largest so far
	if r < N and arr[r] > arr[largest]:
		largest = r

	# If largest is not root
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]

		# Recursively heapify the affected sub-tree
		heapify(arr, N, largest)

# Function to build a Max-Heap from the given array


def buildHeap(arr, N):

	# Index of last non-leaf node
	startIdx = N // 2 - 1

	# Perform reverse level order traversal
	# from last non-leaf node and heapify
	# each node
	for i in range(startIdx, -1, -1):
		heapify(arr, N, i)

# A utility function to print the array
# representation of Heap


def printHeap(arr, N):
	print("Array representation of Heap is:")

	for i in range(N):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':

	# Binary Tree Representation
	# of input array
	#			 1
	#		 / \
	#		 3	 5
	#	 / \	 / \
	#	 4	 6 13 10
	# / \ / \
	# 9 8 15 17
	arr = [1, 3, 5, 4, 6, 13,
		10, 9, 8, 15, 17]

	N = len(arr)

	buildHeap(arr, N)
	printHeap(arr, N)

	# Final Heap:
	#			 17
	#		 / \
	#		 15	 13
	#	 / \	 / \
	#	 9	 6 5 10
	#	 / \ / \
	#	 4 8 3 1

# This code is contributed by Princi Singh
