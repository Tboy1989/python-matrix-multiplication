#!/usr/bin/env python3
"""
Simple Python program for matrix multiplication with logging support
"""

from logger_config import get_logger, log_matrix_operation

def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices using nested loops
    
    Args:
        matrix1: First matrix (list of lists)
        matrix2: Second matrix (list of lists)
    
    Returns:
        Result matrix (list of lists)
    """
    logger = get_logger("core")
    
    # Get dimensions
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    logger.debug(f"Matrix dimensions: A({rows1}x{cols1}), B({rows2}x{cols2})")
    
    # Check if multiplication is possible
    if cols1 != rows2:
        error_msg = f"Cannot multiply matrices: {rows1}x{cols1} and {rows2}x{cols2}"
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    logger.info(f"Starting matrix multiplication: ({rows1}x{cols1}) × ({rows2}x{cols2})")
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    logger.debug(f"Initialized result matrix: {rows1}x{cols2}")
    
    # Perform matrix multiplication
    total_operations = rows1 * cols2 * cols1
    logger.debug(f"Total scalar operations required: {total_operations}")
    
    for i in range(rows1):
        logger.debug(f"Processing row {i+1}/{rows1}")
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    logger.info(f"Matrix multiplication completed successfully: result shape ({rows1}x{cols2})")
    log_matrix_operation("multiply_matrices", (rows1, cols1), (rows2, cols2), (rows1, cols2))
    
    return result

def print_matrix(matrix, name="Matrix"):
    """Print matrix in a formatted way"""
    logger = get_logger("display")
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    
    logger.debug(f"Displaying matrix '{name}' with shape ({rows}x{cols})")
    
    print(f"{name}:")
    for row in matrix:
        print("  [" + ", ".join(f"{num:4}" for num in row) + "]")
    print()

def main():
    """Main demonstration function with logging"""
    logger = get_logger("demo")
    
    logger.info("Starting matrix multiplication demonstration")
    
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
    
    logger.info("Created example matrices for demonstration")
    
    print("Matrix Multiplication Example")
    print("=" * 30)
    
    # Display input matrices
    print_matrix(matrix_a, "Matrix A (2x3)")
    print_matrix(matrix_b, "Matrix B (3x2)")
    
    try:
        # Multiply matrices
        logger.info("Attempting matrix multiplication")
        result = multiply_matrices(matrix_a, matrix_b)
        print_matrix(result, "Result A × B (2x2)")
        
        # Show the calculation for the first element as an example
        print("Calculation example for result[0][0]:")
        calculation = f"{matrix_a[0][0]} × {matrix_b[0][0]} + {matrix_a[0][1]} × {matrix_b[1][0]} + {matrix_a[0][2]} × {matrix_b[2][0]}"
        print(f"  {calculation}")
        
        intermediate = f"{matrix_a[0][0] * matrix_b[0][0]} + {matrix_a[0][1] * matrix_b[1][0]} + {matrix_a[0][2] * matrix_b[2][0]}"
        print(f"  = {intermediate}")
        print(f"  = {result[0][0]}")
        print()
        
        logger.info(f"Demonstration completed successfully. Result[0][0] = {result[0][0]}")
        
    except ValueError as e:
        logger.error(f"Matrix multiplication failed: {e}")
        print(f"Error: {e}")

def numpy_example():
    """Example using NumPy for comparison"""
    logger = get_logger("numpy")
    
    try:
        import numpy as np
        logger.info("NumPy is available, running comparison example")
        
        print("NumPy Alternative:")
        print("-" * 20)
        
        # Same matrices as numpy arrays
        a = np.array([[1, 2, 3], [4, 5, 6]])
        b = np.array([[7, 8], [9, 10], [11, 12]])
        
        logger.debug(f"Created NumPy arrays: A{a.shape}, B{b.shape}")
        
        # Matrix multiplication using NumPy
        logger.info("Performing NumPy matrix multiplication")
        result_np = np.dot(a, b)
        
        print("Matrix A:")
        print(a)
        print("\nMatrix B:")
        print(b)
        print("\nResult (NumPy):")
        print(result_np)
        
        logger.info(f"NumPy multiplication completed: result shape {result_np.shape}")
        log_matrix_operation("numpy.dot", a.shape, b.shape, result_np.shape)
        
    except ImportError as e:
        logger.warning(f"NumPy not available: {e}")
        print("NumPy not available. Install with: pip install numpy")

if __name__ == "__main__":
    # Initialize logging
    from logger_config import configure_logging
    configure_logging("INFO")  # Set to DEBUG for more detailed logs
    
    logger = get_logger("main")
    logger.info("Starting matrix multiplication program")
    
    try:
        main()
        print()
        numpy_example()
        logger.info("Program completed successfully")
    except Exception as e:
        logger.critical(f"Program failed with unexpected error: {e}")
        raise