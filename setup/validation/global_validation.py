import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return bool(re.match(pattern, email))


def validate_bool(value, field_name="field"):
    """
    Converts and validates boolean-like values.
    Accepts: True, False, "true", "false", "1", "0"
    """

    if isinstance(value, bool):
        return value, None
    
    if not value:
        return None, f"{field_name} is required"

    if isinstance(value, str):
        value = value.strip().lower()

        if value in ["true", "1"]:
            return True, None
        if value in ["false", "0"]:
            return False, None

    return None, f"Invalid value for {field_name}"