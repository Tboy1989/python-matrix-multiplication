#!/usr/bin/env python3
"""
Logging configuration module for the matrix multiplication project.
Provides centralized logging setup with console and file output.
"""

import logging
import logging.handlers
import os
import sys
from datetime import datetime
from pathlib import Path


class ColoredFormatter(logging.Formatter):
    """Colored formatter for console output"""
    
    # ANSI color codes
    COLORS = {
        'DEBUG': '\033[36m',     # Cyan
        'INFO': '\033[32m',      # Green
        'WARNING': '\033[33m',   # Yellow
        'ERROR': '\033[31m',     # Red
        'CRITICAL': '\033[35m',  # Magenta
        'RESET': '\033[0m'       # Reset
    }
    
    def format(self, record):
        # Add color to the level name
        level_color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        record.colored_levelname = f"{level_color}{record.levelname}{self.COLORS['RESET']}"
        return super().format(record)


class MatrixLogger:
    """
    Centralized logger configuration for the matrix multiplication project.
    Supports both console and file logging with different formats and levels.
    """
    
    def __init__(self, name="matrix_multiplication", log_dir="logs"):
        self.name = name
        self.log_dir = Path(log_dir)
        self.logger = None
        self._setup_logger()
    
    def _setup_logger(self):
        """Set up the logger with console and file handlers"""
        # Create logger
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        
        # Prevent duplicate handlers if logger is reconfigured
        if self.logger.handlers:
            self.logger.handlers.clear()
        
        # Create log directory if it doesn't exist
        self.log_dir.mkdir(exist_ok=True)
        
        # Setup handlers
        self._setup_console_handler()
        self._setup_file_handlers()
    
    def _setup_console_handler(self):
        """Setup colored console handler"""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        
        # Use colored formatter for console
        console_format = "%(asctime)s | %(colored_levelname)s | %(name)s | %(message)s"
        console_formatter = ColoredFormatter(
            console_format,
            datefmt="%H:%M:%S"
        )
        console_handler.setFormatter(console_formatter)
        
        self.logger.addHandler(console_handler)
    
    def _setup_file_handlers(self):
        """Setup file handlers for different log levels"""
        
        # General log file (INFO and above)
        general_file = self.log_dir / "matrix_multiplication.log"
        file_handler = logging.handlers.RotatingFileHandler(
            general_file,
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        file_handler.setLevel(logging.INFO)
        
        # Debug log file (all levels)
        debug_file = self.log_dir / "matrix_multiplication_debug.log"
        debug_handler = logging.handlers.RotatingFileHandler(
            debug_file,
            maxBytes=50*1024*1024,  # 50MB
            backupCount=3
        )
        debug_handler.setLevel(logging.DEBUG)
        
        # Error log file (ERROR and CRITICAL only)
        error_file = self.log_dir / "matrix_multiplication_errors.log"
        error_handler = logging.handlers.RotatingFileHandler(
            error_file,
            maxBytes=10*1024*1024,  # 10MB
            backupCount=10
        )
        error_handler.setLevel(logging.ERROR)
        
        # File formatter (more detailed)
        file_format = "%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s"
        file_formatter = logging.Formatter(
            file_format,
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        # Set formatters
        file_handler.setFormatter(file_formatter)
        debug_handler.setFormatter(file_formatter)
        error_handler.setFormatter(file_formatter)
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(debug_handler)
        self.logger.addHandler(error_handler)
    
    def get_logger(self):
        """Get the configured logger instance"""
        return self.logger
    
    def set_level(self, level):
        """Set the logging level"""
        if isinstance(level, str):
            level = getattr(logging, level.upper())
        self.logger.setLevel(level)
    
    def log_system_info(self):
        """Log system and environment information"""
        import platform
        import sys
        
        self.logger.info("=" * 50)
        self.logger.info("Matrix Multiplication Logger Initialized")
        self.logger.info("=" * 50)
        self.logger.info(f"Python version: {sys.version}")
        self.logger.info(f"Platform: {platform.platform()}")
        self.logger.info(f"Log directory: {self.log_dir.absolute()}")
        self.logger.info(f"Timestamp: {datetime.now().isoformat()}")
        self.logger.info("=" * 50)


# Global logger instance
_matrix_logger = None


def get_logger(name=None):
    """
    Get the matrix multiplication logger instance.
    
    Args:
        name: Optional logger name suffix
    
    Returns:
        logging.Logger: Configured logger instance
    """
    global _matrix_logger
    
    if _matrix_logger is None:
        _matrix_logger = MatrixLogger()
        _matrix_logger.log_system_info()
    
    if name:
        return logging.getLogger(f"{_matrix_logger.name}.{name}")
    return _matrix_logger.get_logger()


def configure_logging(level="INFO", log_dir="logs"):
    """
    Configure the logging system with custom settings.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_dir: Directory for log files
    """
    global _matrix_logger
    _matrix_logger = MatrixLogger(log_dir=log_dir)
    _matrix_logger.set_level(level)
    _matrix_logger.log_system_info()


# Convenience functions for direct logging
def debug(msg, *args, **kwargs):
    """Log a debug message"""
    get_logger().debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    """Log an info message"""
    get_logger().info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    """Log a warning message"""
    get_logger().warning(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    """Log an error message"""
    get_logger().error(msg, *args, **kwargs)


def critical(msg, *args, **kwargs):
    """Log a critical message"""
    get_logger().critical(msg, *args, **kwargs)


def log_matrix_operation(operation, matrix1_shape, matrix2_shape=None, result_shape=None):
    """
    Log matrix operation details.
    
    Args:
        operation: Name of the operation
        matrix1_shape: Shape of first matrix (rows, cols)
        matrix2_shape: Shape of second matrix (rows, cols)
        result_shape: Shape of result matrix (rows, cols)
    """
    logger = get_logger("operations")
    
    if matrix2_shape and result_shape:
        logger.info(
            f"{operation}: {matrix1_shape} × {matrix2_shape} → {result_shape}"
        )
    else:
        logger.info(f"{operation}: Matrix shape {matrix1_shape}")


if __name__ == "__main__":
    # Test the logger
    configure_logging("DEBUG")
    
    logger = get_logger("test")
    
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    # Test matrix operation logging
    log_matrix_operation("multiply_matrices", (2, 3), (3, 2), (2, 2))
    
    print("Logger test completed. Check the logs/ directory for output files.")