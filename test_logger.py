#!/usr/bin/env python3
"""
Unit tests for the logger configuration module.
Tests logging functionality, file output, and integration.
"""

import pytest
import tempfile
import shutil
import logging
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

from logger_config import (
    MatrixLogger, 
    get_logger, 
    configure_logging,
    log_matrix_operation,
    debug, info, warning, error, critical
)


class TestMatrixLogger:
    """Test class for MatrixLogger"""
    
    def setup_method(self):
        """Set up test environment with temporary directory"""
        self.temp_dir = tempfile.mkdtemp()
        self.log_dir = Path(self.temp_dir) / "test_logs"
    
    def teardown_method(self):
        """Clean up test environment"""
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        # Reset global logger
        import logger_config
        logger_config._matrix_logger = None
    
    def test_matrix_logger_initialization(self):
        """Test basic logger initialization"""
        logger_instance = MatrixLogger(name="test_logger", log_dir=str(self.log_dir))
        
        assert logger_instance.name == "test_logger"
        assert logger_instance.log_dir == self.log_dir
        assert logger_instance.logger is not None
        assert self.log_dir.exists()
    
    def test_log_files_creation(self):
        """Test that log files are created"""
        logger_instance = MatrixLogger(log_dir=str(self.log_dir))
        logger = logger_instance.get_logger()
        
        # Generate some log messages
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")
        
        # Force flush of handlers
        for handler in logger.handlers:
            handler.flush()
        
        # Check that log files exist
        expected_files = [
            "matrix_multiplication.log",
            "matrix_multiplication_debug.log", 
            "matrix_multiplication_errors.log"
        ]
        
        for filename in expected_files:
            log_file = self.log_dir / filename
            assert log_file.exists(), f"Log file {filename} was not created"
    
    def test_log_levels_filtering(self):
        """Test that different log files contain appropriate log levels"""
        logger_instance = MatrixLogger(log_dir=str(self.log_dir))
        logger = logger_instance.get_logger()
        
        # Generate messages at different levels
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")
        
        # Force flush
        for handler in logger.handlers:
            handler.flush()
        
        # Check general log (INFO and above)
        general_log = self.log_dir / "matrix_multiplication.log"
        if general_log.exists():
            content = general_log.read_text()
            assert "Info message" in content
            assert "Warning message" in content
            assert "Error message" in content
            assert "Critical message" in content
            # Debug should not be in general log
            assert "Debug message" not in content
        
        # Check debug log (all levels)
        debug_log = self.log_dir / "matrix_multiplication_debug.log"
        if debug_log.exists():
            content = debug_log.read_text()
            assert "Debug message" in content
            assert "Info message" in content
            assert "Error message" in content
        
        # Check error log (ERROR and CRITICAL only)
        error_log = self.log_dir / "matrix_multiplication_errors.log"
        if error_log.exists():
            content = error_log.read_text()
            assert "Error message" in content
            assert "Critical message" in content
            # Info and debug should not be in error log
            assert "Info message" not in content
            assert "Debug message" not in content
    
    def test_set_level(self):
        """Test setting log level"""
        logger_instance = MatrixLogger(log_dir=str(self.log_dir))
        
        # Test string level
        logger_instance.set_level("WARNING")
        assert logger_instance.logger.level == logging.WARNING
        
        # Test numeric level
        logger_instance.set_level(logging.ERROR)
        assert logger_instance.logger.level == logging.ERROR
    
    def test_log_system_info(self):
        """Test system info logging"""
        with patch('logger_config.datetime') as mock_datetime:
            mock_datetime.now.return_value.isoformat.return_value = "2023-01-01T12:00:00"
            
            logger_instance = MatrixLogger(log_dir=str(self.log_dir))
            
            # Capture log output
            with patch.object(logger_instance.logger, 'info') as mock_info:
                logger_instance.log_system_info()
                
                # Check that system info was logged
                assert mock_info.call_count >= 5  # Multiple info calls
                call_args = [call[0][0] for call in mock_info.call_args_list]
                
                # Check for expected content
                assert any("Matrix Multiplication Logger Initialized" in arg for arg in call_args)
                assert any("Python version" in arg for arg in call_args)
                assert any("Platform" in arg for arg in call_args)


class TestGlobalLoggerFunctions:
    """Test global logger functions"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        # Reset global logger
        import logger_config
        logger_config._matrix_logger = None
    
    def teardown_method(self):
        """Clean up test environment"""
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        # Reset global logger
        import logger_config
        logger_config._matrix_logger = None
    
    def test_get_logger_singleton(self):
        """Test that get_logger returns singleton instance"""
        logger1 = get_logger()
        logger2 = get_logger()
        
        # Should be the same logger instance
        assert logger1 is logger2
    
    def test_get_logger_with_name(self):
        """Test getting logger with specific name"""
        logger = get_logger("test_module")
        assert "test_module" in logger.name
    
    def test_configure_logging(self):
        """Test logging configuration"""
        configure_logging(level="DEBUG", log_dir=str(self.temp_dir))
        
        logger = get_logger()
        assert logger.level == logging.DEBUG
    
    def test_convenience_functions(self):
        """Test convenience logging functions"""
        with patch('logger_config.get_logger') as mock_get_logger:
            mock_logger = MagicMock()
            mock_get_logger.return_value = mock_logger
            
            # Test each convenience function
            debug("Debug message")
            info("Info message")
            warning("Warning message")
            error("Error message")
            critical("Critical message")
            
            # Verify each was called
            mock_logger.debug.assert_called_once_with("Debug message")
            mock_logger.info.assert_called_once_with("Info message")
            mock_logger.warning.assert_called_once_with("Warning message")
            mock_logger.error.assert_called_once_with("Error message")
            mock_logger.critical.assert_called_once_with("Critical message")
    
    def test_log_matrix_operation(self):
        """Test matrix operation logging"""
        with patch('logger_config.get_logger') as mock_get_logger:
            mock_logger = MagicMock()
            mock_get_logger.return_value = mock_logger
            
            # Test with result shape
            log_matrix_operation("test_op", (2, 3), (3, 4), (2, 4))
            mock_logger.info.assert_called_with("test_op: (2, 3) × (3, 4) → (2, 4)")
            
            # Test without result shape
            mock_logger.reset_mock()
            log_matrix_operation("test_op", (2, 3))
            mock_logger.info.assert_called_with("test_op: Matrix shape (2, 3)")


class TestLoggerIntegration:
    """Test logger integration with matrix multiplication"""
    
    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        # Reset global logger
        import logger_config
        logger_config._matrix_logger = None
    
    def teardown_method(self):
        """Clean up test environment"""
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        # Reset global logger
        import logger_config
        logger_config._matrix_logger = None
    
    def test_matrix_multiplication_logging(self):
        """Test that matrix multiplication generates appropriate logs"""
        configure_logging(level="DEBUG", log_dir=str(self.temp_dir))
        
        # Import after configuration
        from matrix_multiplication import multiply_matrices
        
        # Perform matrix multiplication
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        
        # Use patch on the matrix_multiplication module directly
        with patch('matrix_multiplication.get_logger') as mock_get_logger:
            mock_logger = MagicMock()
            mock_get_logger.return_value = mock_logger
            
            result = multiply_matrices(matrix1, matrix2)
            
            # Verify logging calls were made
            assert mock_logger.debug.call_count >= 2  # At least dimension and initialization logs
            assert mock_logger.info.call_count >= 2   # Start and completion logs
    
    def test_error_logging(self):
        """Test that errors are properly logged"""
        configure_logging(level="DEBUG", log_dir=str(self.temp_dir))
        
        from matrix_multiplication import multiply_matrices
        
        # Try incompatible matrices
        matrix1 = [[1, 2]]      # 1x2
        matrix2 = [[1], [2], [3]]  # 3x1
        
        with patch('matrix_multiplication.get_logger') as mock_get_logger:
            mock_logger = MagicMock()
            mock_get_logger.return_value = mock_logger
            
            with pytest.raises(ValueError):
                multiply_matrices(matrix1, matrix2)
            
            # Verify error was logged
            mock_logger.error.assert_called()
            error_call = mock_logger.error.call_args[0][0]
            assert "Cannot multiply matrices" in error_call


class TestColoredFormatter:
    """Test colored formatter for console output"""
    
    def test_colored_formatter(self):
        """Test that ColoredFormatter adds colors to log records"""
        from logger_config import ColoredFormatter
        
        formatter = ColoredFormatter("%(colored_levelname)s: %(message)s")
        
        # Create a test record
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname="",
            lineno=0,
            msg="Test message",
            args=(),
            exc_info=None
        )
        
        formatted = formatter.format(record)
        
        # Should contain ANSI color codes
        assert "\033[32m" in formatted  # Green color for INFO
        assert "\033[0m" in formatted   # Reset color
        assert "INFO" in formatted
        assert "Test message" in formatted


if __name__ == "__main__":
    # Run the logger tests
    pytest.main([__file__, "-v"])