# arithmetic_server.py
from mcp.server.fastmcp import FastMCP
import operator

mcp = FastMCP("Arithmetic")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    return operator.add(a, b)

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a"""
    return operator.sub(a, b)

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together"""
    return operator.mul(a, b)

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b"""
    if b == 0:
        return "Error: Division by zero"
    return operator.truediv(a, b)

if __name__ == "__main__":
    mcp.run(transport="stdio")
