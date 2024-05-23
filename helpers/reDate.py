import re

def is_valid_date(date_string):
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    if pattern.match(date_string):
        return True
    else:
        return False