import numpy as np

matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(matrix1)

def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer -1
        for i in range(first,last):
            # saving top element into a temporary variable
            top = matrix[layer][i]
            # moving left element to the top
            matrix[layer][i] = matrix[-i-1][layer]
            # moving bottom element to the left
            matrix[-i - 1][layer] = matrix[-layer-1][-i-1]
            # moving right element to the bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer-1]
            # moving top to the right
            matrix[i][-layer - 1] = top
        return matrix
print("After Rotation")
print(rotateMatrix(matrix1))
