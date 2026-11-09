#Simple Calculator Module for CI Pipeline Demonstration
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

if __name__ == "__main__":
    print("Application started...")
    print(f"2 + 3 = {add_numbers(2, 3)}")