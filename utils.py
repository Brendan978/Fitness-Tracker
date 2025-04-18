from datetime import datetime

def format_date(date_str):
    """
    Converts 'YYYY-MM-DD' to 'Mon DD, YYYY' (e.g., '2025-04-18' → 'Apr 18, 2025').
    Returns 'Invalid date' if input is wrong.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d, %Y")
    except ValueError:
        return "Invalid date"

def get_int_input(prompt):
    """
    Repeatedly asks for input until a valid integer is entered.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
