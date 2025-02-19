from timespy import timer
import time
# Usage example: exec_time is now accessible as a function attribute
@timer
def slow_function():
    time.sleep(2)

slow_function()  # Execute function

# ✅ Execution time can also be accessed after calling the function
print(f">>> {slow_function.__name__} Execution time : {slow_function.exec_time:.6f}s")
