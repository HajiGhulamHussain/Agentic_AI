from agents import function_tool

@function_tool
def plus(n1: int, n2: int) -> str:
    """
    This is plus function
        arg:
            n1:int
            n2:int
        return str
    """
    print("plus Tool Fire --->")
    return f"your answer is: {n1 + n2}"

@function_tool
def subtract(n1: int, n2: int) -> str:
    print("subtract Tool Fire --->")
    return f"your answer is: {n1 - n2}"

@function_tool
def multiply(n1: int, n2: int) -> str:
    print("multiply Tool Fire --->")
    return f"your answer is: {n1 * n2}"

@function_tool
def divide(n1: int, n2: int) -> str:
    print("divide Tool Fire --->")
    return f"your answer is: {n1 / n2}"
