import os
api_key = os.getenv("DEMO_API_KEY", "not_set")


def add(a: int, b: int) -> int:
    """Add two integers and return the result.
    Args:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        int: The sum of a and b.
    """
    # For demonstration, print or use the API key
    print(f"DEMO_API_KEY: {api_key}")
    return a + b
