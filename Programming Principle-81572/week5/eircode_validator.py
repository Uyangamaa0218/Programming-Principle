import re

def has_eircode_shape(value):
    if not isinstance(value, str):
        return False
    return re.fullmatch(r"[A-Za-z0-9]{3} [A-Za-z0-9]{4}", value) is not None 