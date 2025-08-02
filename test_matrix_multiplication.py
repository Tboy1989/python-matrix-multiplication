#!/usr/bin/env python3
"""
Unit tests for matrix multiplication using pytest
Achieves 100% code coverage for the multiply_matrices function
"""

import pytest
from matrix_multiplication import multiply_matrices


class TestMultiplyMatrices:
    """Test class for multiply_matrices function"""
    
    def test_basic_multiplication_2x3_and_3x2(self):
        """Test basic 2x3 and 3x2 matrix multiplication"""
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[7, 8], [9, 10], [11, 12]]
        expected = [[58, 64], [139, 154]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_square_matrix_multiplication_2x2(self):
        """Test 2x2 square matrix multiplication"""
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_single_element_matrices_1x1(self):
        """Test 1x1 matrix multiplication"""
        matrix1 = [[5]]
        matrix2 = [[3]]
        expected = [[15]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_single_row_and_single_column(self):
        """Test 1x3 and 3x1 matrix multiplication"""
        matrix1 = [[1, 2, 3]]
        matrix2 = [[4], [5], [6]]
        expected = [[32]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_single_column_and_single_row(self):
        """Test 3x1 and 1x3 matrix multiplication"""
        matrix1 = [[1], [2], [3]]
        matrix2 = [[4, 5, 6]]
        expected = [[4, 5, 6], [8, 10, 12], [12, 15, 18]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_matrices_with_zeros(self):
        """Test multiplication with matrices containing zeros"""
        matrix1 = [[0, 1], [2, 0]]
        matrix2 = [[1, 0], [0, 3]]
        expected = [[0, 3], [2, 0]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_matrices_with_negative_numbers(self):
        """Test multiplication with negative numbers"""
        matrix1 = [[-1, 2], [3, -4]]
        matrix2 = [[1, -2], [-3, 4]]
        expected = [[-7, 10], [15, -22]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_matrices_with_floats(self):
        """Test multiplication with floating point numbers"""
        matrix1 = [[1.5, 2.5], [3.5, 4.5]]
        matrix2 = [[0.5, 1.5], [2.5, 3.5]]
        expected = [[7.0, 11.0], [13.0, 21.0]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_identity_matrix_multiplication(self):
        """Test multiplication with identity matrix"""
        matrix1 = [[1, 2], [3, 4]]
        identity = [[1, 0], [0, 1]]
        expected = [[1, 2], [3, 4]]
        
        result = multiply_matrices(matrix1, identity)
        assert result == expected
    
    def test_zero_matrix_multiplication(self):
        """Test multiplication with zero matrix"""
        matrix1 = [[1, 2], [3, 4]]
        zero_matrix = [[0, 0], [0, 0]]
        expected = [[0, 0], [0, 0]]
        
        result = multiply_matrices(matrix1, zero_matrix)
        assert result == expected
    
    def test_larger_matrix_multiplication_3x4_and_4x2(self):
        """Test larger matrix multiplication: 3x4 and 4x2"""
        matrix1 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        matrix2 = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ]
        expected = [
            [50, 60],
            [114, 140],
            [178, 220]
        ]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_incompatible_dimensions_raises_error(self):
        """Test that incompatible matrix dimensions raise ValueError"""
        matrix1 = [[1, 2], [3, 4]]  # 2x2
        matrix2 = [[1, 2, 3]]       # 1x3
        
        with pytest.raises(ValueError) as exc_info:
            multiply_matrices(matrix1, matrix2)
        
        assert "Cannot multiply matrices: 2x2 and 1x3" in str(exc_info.value)
    
    def test_another_incompatible_dimensions(self):
        """Test another case of incompatible dimensions"""
        matrix1 = [[1, 2, 3]]       # 1x3
        matrix2 = [[1, 2], [3, 4]]  # 2x2
        
        with pytest.raises(ValueError) as exc_info:
            multiply_matrices(matrix1, matrix2)
        
        assert "Cannot multiply matrices: 1x3 and 2x2" in str(exc_info.value)
    
    def test_large_incompatible_dimensions(self):
        """Test incompatible dimensions with larger matrices"""
        matrix1 = [[1, 2, 3, 4, 5]]  # 1x5
        matrix2 = [[1], [2], [3]]     # 3x1
        
        with pytest.raises(ValueError) as exc_info:
            multiply_matrices(matrix1, matrix2)
        
        assert "Cannot multiply matrices: 1x5 and 3x1" in str(exc_info.value)
    
    def test_mixed_positive_negative_zero(self):
        """Test matrix with mix of positive, negative, and zero values"""
        matrix1 = [[-1, 0, 3], [2, -5, 0]]
        matrix2 = [[4, -2], [0, 1], [-3, 2]]
        expected = [[-13, 8], [8, -9]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_very_small_matrices_1x2_and_2x1(self):
        """Test very small matrices: 1x2 and 2x1"""
        matrix1 = [[7, 3]]
        matrix2 = [[2], [4]]
        expected = [[26]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected


class TestMatrixMultiplicationEdgeCases:
    """Additional edge case tests"""
    
    def test_single_element_with_zero(self):
        """Test single element matrix with zero"""
        matrix1 = [[0]]
        matrix2 = [[5]]
        expected = [[0]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_rectangular_matrices_4x1_and_1x4(self):
        """Test 4x1 and 1x4 matrix multiplication"""
        matrix1 = [[1], [2], [3], [4]]
        matrix2 = [[5, 6, 7, 8]]
        expected = [
            [5, 6, 7, 8],
            [10, 12, 14, 16],
            [15, 18, 21, 24],
            [20, 24, 28, 32]
        ]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected
    
    def test_large_numbers(self):
        """Test multiplication with large numbers"""
        matrix1 = [[1000, 2000]]
        matrix2 = [[3000], [4000]]
        expected = [[11000000]]
        
        result = multiply_matrices(matrix1, matrix2)
        assert result == expected


if __name__ == "__main__":
    # Run tests with coverage
    pytest.main([__file__, "-v", "--cov=matrix_multiplication", "--cov-report=term-missing"])