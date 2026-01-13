import random
from fastmcp import FastMCP
from threading import Thread

weather_mcp = FastMCP("Weather MCP")
math_mcp = FastMCP("Math MCP")

@weather_mcp.tool()
def get_weather(city: str) -> str:
    """
    Retrieves the current weather for a specified city.
    
    Args:
        city: The name of the city to check.
    """
    conditions = ["Sunny", "Cloudy", "Rainy", "Snowing", "Windy"]
    temp = random.randint(-10, 35)
    condition = random.choice(conditions)
    
    return f"The current weather in {city} is {condition} at {temp}°C."

@math_mcp.tool()
def sum_numbers(a: float, b: float) -> float:
    """
    Adds two numbers together.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    def run_weather():
        weather_mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")
    
    def run_math():
        math_mcp.run(transport="http", host="127.0.0.1", port=8001, path="/mcp")
    
    # Start weather service in a separate thread
    weather_thread = Thread(target=run_weather, daemon=True)
    weather_thread.start()
    
    # Run math service in the main thread
    run_math()