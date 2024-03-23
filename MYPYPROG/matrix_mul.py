def multiply_matrices(A, B):
    """Multiplies two 3x3 matrices.

    Args:
        A: A 3x3 matrix.
        B: A 3x3 matrix.

    Returns:
        The product of A and B.
    """

    if len(A) != 3 or len(A[0]) != 3 or len(B) != 3 or len(B[0]) != 3:
        raise ValueError("Both matrices must be 3x3")

    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result


# Example usage:

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]

result = multiply_matrices(A, B)

print(result)
