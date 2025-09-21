def check_age_limit(age: int) -> bool:
    """Checks if age is above 18

    Args:
        age (int): Age of a person

    Returns:
        bool: True if age >= 18, False otherwise
    """
    if age >= 18:
        return True
    else:
        return False
