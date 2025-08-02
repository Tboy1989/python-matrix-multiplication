#!/usr/bin/env python3
"""
Simple Python program for matrix multiplication
"""

def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices using nested loops
    
    Args:
        matrix1: First matrix (list of lists)
        matrix2: Second matrix (list of lists)
    
    Returns:
        Result matrix (list of lists)
    """
    # Get dimensions
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    # Check if multiplication is possible
    if cols1 != rows2:
        raise ValueError(f"Cannot multiply matrices: {rows1}x{cols1} and {rows2}x{cols2}")
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def print_matrix(matrix, name="Matrix"):
    """Print matrix in a formatted way"""
    print(f"{name}:")
    for row in matrix:
        print("  [" + ", ".join(f"{num:4}" for num in row) + "]")
    print()

def main():
    # Example matrices
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    matrix_b = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    
    print("Matrix Multiplication Example")
    print("=" * 30)
    
    # Display input matrices
    print_matrix(matrix_a, "Matrix A (2x3)")
    print_matrix(matrix_b, "Matrix B (3x2)")
    
    try:
        # Multiply matrices
        result = multiply_matrices(matrix_a, matrix_b)
        print_matrix(result, "Result A × B (2x2)")
        
        # Show the calculation for the first element as an example
        print("Calculation example for result[0][0]:")
        print(f"  {matrix_a[0][0]} × {matrix_b[0][0]} + {matrix_a[0][1]} × {matrix_b[1][0]} + {matrix_a[0][2]} × {matrix_b[2][0]}")
        print(f"  = {matrix_a[0][0] * matrix_b[0][0]} + {matrix_a[0][1] * matrix_b[1][0]} + {matrix_a[0][2] * matrix_b[2][0]}")
        print(f"  = {result[0][0]}")
        print()
        
    except ValueError as e:
        print(f"Error: {e}")

def numpy_example():
    """Example using NumPy for comparison"""
    try:
        import numpy as np
        
        print("NumPy Alternative:")
        print("-" * 20)
        
        # Same matrices as numpy arrays
        a = np.array([[1, 2, 3], [4, 5, 6]])
        b = np.array([[7, 8], [9, 10], [11, 12]])
        
        # Matrix multiplication using NumPy
        result_np = np.dot(a, b)
        
        print("Matrix A:")
        print(a)
        print("\nMatrix B:")
        print(b)
        print("\nResult (NumPy):")
        print(result_np)
        
    except ImportError:
        print("NumPy not available. Install with: pip install numpy")

if __name__ == "__main__":
    main()
    print()
    numpy_example()