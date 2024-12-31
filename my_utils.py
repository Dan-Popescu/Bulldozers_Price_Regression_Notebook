import matplotlib.ticker as mticker

def format_to_dollars(value, tick_number):
    """
    Format a numeric value as dollars with spaces for thousands.

    Args:
        value (float): The value to format.
        tick_number (int): Tick number (not used but required by FuncFormatter).

    Returns:
        str: Formatted string with a dollar sign and spaces between thousands.
    """
    return f"$ {int(value):,}".replace(",", " ")
