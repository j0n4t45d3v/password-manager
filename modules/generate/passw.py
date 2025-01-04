import secrets
import string

LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL_CHAR = string.punctuation


def generate_password(quantity_letters, quantity_digits, quantity_special_chars) -> str:
    letters: str = get_random_chars(LETTERS, quantity_letters)
    digits: str = get_random_chars(DIGITS, quantity_digits)
    special_chars: str = get_random_chars(SPECIAL_CHAR, quantity_special_chars)
    combined: str = letters + digits + special_chars
    return shuffle_string(combined)


def get_random_chars(chars: str, lenght: int) -> str:
    return "".join([secrets.choice(chars) for _ in range(lenght)])


def shuffle_string(value: str) -> str:
    list_chars: list = list(value)
    secrets.SystemRandom().shuffle(list_chars)
    return "".join(list_chars)
