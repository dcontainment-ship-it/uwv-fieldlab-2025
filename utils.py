from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def is_valid_bsn(bsn :str) -> bool:
    """
    Validate a Dutch BSN using the 11-proof rule:
    - Digits are multiplied by their position from left to right
    - The last digit is multiplied by -1
    - The sum modulo 11 should be 0

    """
    if not bsn.isdigit():
        print("Invalid BSN: contains non-digit characters.")
        return False
    if len(bsn) not in (8, 9):
        print("Invalid BSN: must be 8 or 9 digits long.")
        return False

    total = 0
    length = len(bsn)

    # Multiply each digit by its weight (position), last digit negative
    for i, digit in enumerate(bsn):
        weight = length - i if i != length - 1 else -1
        total += int(digit) * weight
    return total % 11 == 0
