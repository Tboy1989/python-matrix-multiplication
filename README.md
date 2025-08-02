# Matrix Multiplication in Python

A simple yet comprehensive Python implementation of matrix multiplication with extensive testing coverage.

## 📋 Overview

This project provides a pure Python implementation of matrix multiplication using nested loops, along with comprehensive unit tests that achieve 100% code coverage. The implementation includes educational examples and demonstrates both manual computation and NumPy alternatives.

## 🚀 Features

- **Pure Python Implementation**: No external dependencies required for core functionality
- **Comprehensive Error Handling**: Validates matrix dimensions and provides clear error messages
- **Educational Examples**: Step-by-step calculation demonstrations
- **NumPy Comparison**: Shows equivalent operations using NumPy (when available)
- **100% Test Coverage**: Extensive pytest suite covering all edge cases
- **Multiple Data Types**: Supports integers, floats, negative numbers, and zero values
- **GitHub MCP Integration**: Enhanced development workflow with GitHub repository management

## 📁 Project Structure

```
mcp-demo/
├── matrix_multiplication.py      # Main implementation
├── test_matrix_multiplication.py # Comprehensive test suite
├── mcp.json                      # MCP server configuration
├── GITHUB_MCP_SETUP.md          # GitHub MCP setup guide
├── .gitignore                    # Git ignore patterns
└── README.md                    # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone or download the project files
2. Install testing dependencies (optional):
   ```bash
   pip install pytest pytest-cov
   ```
3. Install NumPy for enhanced examples (optional):
   ```bash
   pip install numpy
   ```

## 💻 Usage

### Basic Usage

```python
from matrix_multiplication import multiply_matrices

# Define two matrices
matrix_a = [[1, 2, 3], [4, 5, 6]]      # 2x3 matrix
matrix_b = [[7, 8], [9, 10], [11, 12]] # 3x2 matrix

# Multiply matrices
result = multiply_matrices(matrix_a, matrix_b)
print(result)  # Output: [[58, 64], [139, 154]]
```

### Running the Demo

Execute the main program to see a complete demonstration:

```bash
python3 matrix_multiplication.py
```

**Sample Output:**
```
Matrix Multiplication Example
==============================
Matrix A (2x3):
  [   1,    2,    3]
  [   4,    5,    6]

Matrix B (3x2):
  [   7,    8]
  [   9,   10]
  [  11,   12]

Result A × B (2x2):
  [  58,   64]
  [ 139,  154]

Calculation example for result[0][0]:
  1 × 7 + 2 × 9 + 3 × 11
  = 7 + 18 + 33
  = 58
```

## 📊 Core Function: `multiply_matrices`

### Function Signature
```python
def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices using nested loops
    
    Args:
        matrix1: First matrix (list of lists)
        matrix2: Second matrix (list of lists)
    
    Returns:
        Result matrix (list of lists)
    
    Raises:
        ValueError: If matrix dimensions are incompatible
    """
```

### Matrix Multiplication Rules

For matrix multiplication `A × B = C`:
- **Dimension Requirements**: A must be `m×n` and B must be `n×p` to produce C as `m×p`
- **Element Calculation**: `C[i][j] = Σ(A[i][k] × B[k][j])` for k from 0 to n-1

### Supported Matrix Types

- ✅ Square matrices (n×n)
- ✅ Rectangular matrices (m×n)
- ✅ Single row/column matrices
- ✅ Single element matrices (1×1)
- ✅ Identity matrices
- ✅ Zero matrices

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest test_matrix_multiplication.py -v

# Run tests with coverage report
pytest test_matrix_multiplication.py --cov=matrix_multiplication --cov-report=term-missing

# Generate HTML coverage report
pytest test_matrix_multiplication.py --cov=matrix_multiplication --cov-report=html
```

### Test Coverage

The test suite includes **19 comprehensive test cases** covering:

#### ✅ **Normal Operations**
- Various matrix dimension combinations (2×3, 3×2, 2×2, etc.)
- Different data types (integers, floats, negatives)
- Identity and zero matrix operations

#### ✅ **Edge Cases**
- Single element matrices (1×1)
- Single row/column matrices
- Large matrices
- Matrices with mixed positive/negative/zero values

#### ✅ **Error Handling**
- Incompatible matrix dimensions
- Proper error message validation
- Multiple error scenarios

#### ✅ **Coverage Statistics**
- **100% coverage** of the `multiply_matrices` function
- **All 19 tests pass**
- **Comprehensive validation** of all code paths

## 🔍 Example Test Cases

```python
# Basic multiplication
multiply_matrices([[1, 2]], [[3], [4]])  # Result: [[11]]

# Square matrices
multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])  # Result: [[19, 22], [43, 50]]

# Error case - incompatible dimensions
multiply_matrices([[1, 2]], [[1, 2, 3]])  # Raises ValueError
```

## 🏗️ Implementation Details

### Algorithm
The implementation uses the standard **triple nested loop** approach:
1. **Outer loop**: Iterates through rows of the first matrix
2. **Middle loop**: Iterates through columns of the second matrix  
3. **Inner loop**: Performs dot product calculation

### Time Complexity
- **O(m × n × p)** where matrices are `m×n` and `n×p`
- **Space Complexity**: O(m × p) for the result matrix

### Key Features
- **Input Validation**: Checks matrix compatibility before computation
- **Clean Error Messages**: Provides clear dimension information in errors
- **Memory Efficient**: Initializes result matrix with appropriate dimensions
- **Type Flexible**: Works with any numeric Python types

## 🔬 Mathematical Background

Matrix multiplication is a fundamental operation in linear algebra where the element at position `(i,j)` in the result matrix is computed as the dot product of the `i`-th row of the first matrix and the `j`-th column of the second matrix.

**Formula**: For matrices A(m×n) and B(n×p) producing C(m×p):
```
C[i][j] = Σ(k=0 to n-1) A[i][k] × B[k][j]
```

## 🐍 NumPy Alternative

The program also demonstrates equivalent operations using NumPy:

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])
result = np.dot(a, b)  # or a @ b in Python 3.5+
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass with 100% coverage
6. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🔍 Troubleshooting

### Common Issues

**ValueError: Cannot multiply matrices**
- **Cause**: Matrix dimensions are incompatible
- **Solution**: Ensure first matrix columns = second matrix rows

**Import Error**
- **Cause**: Missing dependencies for testing
- **Solution**: Install pytest: `pip install pytest pytest-cov`

**NumPy not available warning**
- **Cause**: NumPy not installed (optional)
- **Solution**: Install NumPy: `pip install numpy`

## 🔗 GitHub MCP Integration

This project includes GitHub MCP (Model Context Protocol) server integration for enhanced development workflow capabilities.

### Quick Setup
1. See `GITHUB_MCP_SETUP.md` for detailed setup instructions
2. Configure your GitHub Personal Access Token
3. Copy `mcp.json` to your Cursor MCP configuration

### Available Capabilities
- Repository management and file operations
- Issue and pull request creation
- Code search across GitHub
- Branch management and collaboration features

## 📞 Support

For questions or issues:
1. Check the test cases for usage examples
2. Review the mathematical background section
3. Run the demo program for interactive examples
4. Examine the comprehensive test suite for edge cases
5. For GitHub MCP setup issues, see `GITHUB_MCP_SETUP.md`

---

**Project Status**: ✅ Complete with 100% test coverage and GitHub MCP integration