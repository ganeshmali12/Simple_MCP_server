
import asyncio          # For handling asynchronous operations (tasks that wait for responses)
import httpx            # For making HTTP requests to external APIs
from datetime import datetime  # For working with dates and times
from mcp.server.fastmcp import FastMCP  # The MCP framework for creating tools

# Initialize server
mcp = FastMCP("my-tools")


@mcp.tool()
async def get_current_time(timezone: str = "UTC") -> str:
    """Get the current time.
    
    Args:
        timezone: Timezone name (e.g., 'UTC', 'America/New_York', 'Asia/Tokyo')
    """
    now = datetime.now()
    return f"Current time in {timezone}: {now.strftime('%Y-%m-%d %H:%M:%S')}"


@mcp.tool()
async def calculate(expression: str) -> str:
    """Calculate a mathematical expression safely.
    
    Args:
        expression: Math expression to evaluate (e.g., '2 + 2', '10 * 5')
    """
    try:
        # Safe evaluation - only allows basic math
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            return "Error: Only basic math operations allowed (+, -, *, /, parentheses)"
        
        result = eval(expression, {"__builtins__": {}}, {})
        return f"{expression} = {result}"
    except Exception as e:
        return f"Error calculating: {str(e)}"


@mcp.tool()
async def get_random_fact() -> str:
    """Get a random interesting fact from an API."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en",  # Fixed URL
                timeout=10.0
            )
            response.raise_for_status()
            data = response.json()
            return f"Random Fact: {data['text']}"
        except Exception as e:
            return f"Couldn't fetch a fact right now. Error: {str(e)}"


@mcp.tool()
async def word_count(text: str) -> str:
    """Count words, characters, and sentences in text.
    
    Args:
        text: The text to analyze
    """
    words = len(text.split())
    chars = len(text)
    chars_no_spaces = len(text.replace(" ", ""))
    sentences = text.count('.') + text.count('!') + text.count('?')
    
    return f"""Text Analysis:
- Words: {words}
- Characters (with spaces): {chars}
- Characters (no spaces): {chars_no_spaces}
- Sentences: {sentences}"""


def main():
    """Run the MCP server."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()