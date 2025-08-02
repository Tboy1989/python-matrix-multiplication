#!/usr/bin/env python3
"""
Demonstration script for the matrix multiplication logging system.
Shows various logging features and capabilities.
"""

from logger_config import configure_logging, get_logger
from matrix_multiplication import multiply_matrices
import time


def demonstrate_logging_levels():
    """Demonstrate different logging levels"""
    logger = get_logger("demo")
    
    print("=" * 60)
    print("LOGGING LEVELS DEMONSTRATION")
    print("=" * 60)
    
    logger.debug("🔍 DEBUG: This is a debug message - detailed information for troubleshooting")
    logger.info("ℹ️  INFO: This is an info message - general information about program flow")
    logger.warning("⚠️  WARNING: This is a warning message - something unexpected but not critical")
    logger.error("❌ ERROR: This is an error message - something went wrong but recoverable")
    logger.critical("🚨 CRITICAL: This is a critical message - serious error, program may stop")
    
    print("\nCheck the logs/ directory for file outputs!\n")


def demonstrate_matrix_operations():
    """Demonstrate matrix operations with logging"""
    logger = get_logger("matrix_demo")
    
    print("=" * 60)
    print("MATRIX OPERATIONS WITH LOGGING")
    print("=" * 60)
    
    # Test case 1: Successful multiplication
    logger.info("Starting matrix operations demonstration")
    
    matrix_a = [[1, 2, 3], [4, 5, 6]]
    matrix_b = [[7, 8], [9, 10], [11, 12]]
    
    print("Test 1: Valid matrix multiplication")
    print(f"Matrix A: {matrix_a}")
    print(f"Matrix B: {matrix_b}")
    
    try:
        result = multiply_matrices(matrix_a, matrix_b)
        print(f"Result: {result}")
        logger.info("Matrix multiplication test 1 completed successfully")
    except Exception as e:
        logger.error(f"Matrix multiplication test 1 failed: {e}")
    
    print("\n" + "-" * 40 + "\n")
    
    # Test case 2: Error case
    print("Test 2: Invalid matrix multiplication (incompatible dimensions)")
    
    matrix_c = [[1, 2]]
    matrix_d = [[1, 2, 3], [4, 5, 6]]
    
    print(f"Matrix C: {matrix_c}")
    print(f"Matrix D: {matrix_d}")
    
    try:
        result = multiply_matrices(matrix_c, matrix_d)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Expected error occurred: {e}")
        logger.info("Error case handled correctly")
    
    print("\n")


def demonstrate_performance_logging():
    """Demonstrate performance logging with larger matrices"""
    logger = get_logger("performance")
    
    print("=" * 60)
    print("PERFORMANCE LOGGING DEMONSTRATION")
    print("=" * 60)
    
    # Create larger matrices for performance testing
    size = 50
    matrix_large_a = [[i + j for j in range(size)] for i in range(size)]
    matrix_large_b = [[i * j if j > 0 else 1 for j in range(size)] for i in range(size)]
    
    logger.info(f"Starting performance test with {size}x{size} matrices")
    print(f"Testing matrix multiplication with {size}x{size} matrices...")
    
    start_time = time.time()
    
    try:
        result = multiply_matrices(matrix_large_a, matrix_large_b)
        end_time = time.time()
        
        duration = end_time - start_time
        operations = size * size * size  # Total scalar multiplications
        
        logger.info(f"Performance test completed in {duration:.4f} seconds")
        logger.info(f"Total operations: {operations:,}")
        logger.info(f"Operations per second: {operations/duration:,.0f}")
        
        print(f"✅ Completed in {duration:.4f} seconds")
        print(f"📊 Total operations: {operations:,}")
        print(f"⚡ Operations per second: {operations/duration:,.0f}")
        
    except Exception as e:
        logger.error(f"Performance test failed: {e}")
        print(f"❌ Performance test failed: {e}")
    
    print("\n")


def demonstrate_log_file_contents():
    """Show what's in the log files"""
    import os
    from pathlib import Path
    
    print("=" * 60)
    print("LOG FILES CONTENT PREVIEW")
    print("=" * 60)
    
    log_dir = Path("logs")
    
    if not log_dir.exists():
        print("No logs directory found. Run some operations first!")
        return
    
    log_files = [
        ("General Log", "matrix_multiplication.log"),
        ("Debug Log", "matrix_multiplication_debug.log"),
        ("Error Log", "matrix_multiplication_errors.log")
    ]
    
    for name, filename in log_files:
        file_path = log_dir / filename
        if file_path.exists():
            print(f"\n{name} ({filename}):")
            print("-" * 40)
            try:
                content = file_path.read_text()
                # Show last 5 lines
                lines = content.strip().split('\n')
                for line in lines[-5:]:
                    if line.strip():
                        print(f"  {line}")
                
                print(f"  ... (showing last 5 lines, total: {len(lines)} lines)")
            except Exception as e:
                print(f"  Could not read file: {e}")
        else:
            print(f"\n{name}: File not found")
    
    print("\n")


def main():
    """Main demonstration function"""
    print("🔬 Matrix Multiplication Logging System Demo")
    print("=" * 60)
    
    # Configure logging for demonstration
    print("Configuring logging system...")
    configure_logging(level="DEBUG", log_dir="logs")
    
    main_logger = get_logger("main")
    main_logger.info("Starting logging demonstration")
    
    try:
        # Run demonstrations
        demonstrate_logging_levels()
        time.sleep(0.5)  # Small delay between demos
        
        demonstrate_matrix_operations()
        time.sleep(0.5)
        
        demonstrate_performance_logging()
        time.sleep(0.5)
        
        demonstrate_log_file_contents()
        
        main_logger.info("Logging demonstration completed successfully")
        print("✅ Demonstration completed! Check the logs/ directory for detailed logs.")
        
    except Exception as e:
        main_logger.critical(f"Demonstration failed: {e}")
        print(f"❌ Demonstration failed: {e}")
        raise


if __name__ == "__main__":
    main()