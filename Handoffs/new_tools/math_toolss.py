from agents import function_tool,RunContextWrapper

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


# decorator
@function_tool
def get_age(ctx:RunContextWrapper):
    """Get Age"""
    print("get age fire --->")
    print("ctx fire {ctx}")
    return f"your age is:{ctx.context["name"]}"