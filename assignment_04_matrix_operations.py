# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =======================================================================

#function to read a matrix from user input
def read_matrix(rows, cols, name):
    """Read a matrix from user input."""
    matrix = []
    print(f"Enter {name} matrix ({rows} x {cols}):")
    for i in range(rows):
        while True:
            row = input(f"Enter row {i+1}: ").strip().split()
            if len(row) == cols:
                try:
                    matrix.append([int(x) for x in row])
                    break
                except ValueError:
                    print("Please enter valid integers.")
            else:
                print(f"Please enter exactly {cols} numbers.")
    return matrix


def print_matrix(matrix, title=""):
    """Display a matrix in neat aligned grid format."""
    if title:
        print(title)
    if not matrix:
        print("Empty matrix")
        return
    
    # Find max width for alignment
    max_width = max(len(str(num)) for row in matrix for num in row)
    
    for row in matrix:
        print(" ".join(f"{num:>{max_width}}" for num in row))
    print()


def transpose_matrix(matrix):
    """Return the transpose of the given matrix."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the product of matrix A (M x N) and matrix B (N x P)."""
    m = len(matrix_a)
    n = len(matrix_a[0])
    p = len(matrix_b[0])
    
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


# ============ PART A – Transpose a Matrix ============
print("=" * 50)
print("PART A – TRANSPOSE A MATRIX")
print("=" * 50)

rows_a = int(input("Enter number of rows: "))
cols_a = int(input("Enter number of columns: "))

matrix_a = read_matrix(rows_a, cols_a, "A")

print_matrix(matrix_a, "Original Matrix A:")
transposed = transpose_matrix(matrix_a)
print_matrix(transposed, "Transposed Matrix A^T:")


# ============ PART B – Add Two Matrices ============
print("=" * 50)
print("PART B – ADD TWO MATRICES")
print("=" * 50)

rows_b = int(input("Enter number of rows: "))
cols_b = int(input("Enter number of columns: "))

matrix_b = read_matrix(rows_b, cols_b, "B")
matrix_c = read_matrix(rows_b, cols_b, "C")

print_matrix(matrix_b, "Matrix B:")
print_matrix(matrix_c, "Matrix C:")

sum_matrix = add_matrices(matrix_b, matrix_c)
print_matrix(sum_matrix, "Sum (B + C):")


# ============ PART C – Multiply Two Matrices ============
print("=" * 50)
print("PART C – MULTIPLY TWO MATRICES")
print("=" * 50)

m = int(input("Enter number of rows for matrix A (M): "))
n = int(input("Enter number of columns for matrix A / rows for matrix B (N): "))
p = int(input("Enter number of columns for matrix B (P): "))

matrix_m1 = read_matrix(m, n, "A")
matrix_m2 = read_matrix(n, p, "B")

print_matrix(matrix_m1, "Matrix A (M x N):")
print_matrix(matrix_m2, "Matrix B (N x P):")

product = multiply_matrices(matrix_m1, matrix_m2)
print_matrix(product, f"Product A x B ({m} x {p}):")