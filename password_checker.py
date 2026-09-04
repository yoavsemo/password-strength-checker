from getpass import getpass
from enum import Enum


class PasswordStrength(Enum):
    WEAK = 1
    MODERATE = 2
    STRONG = 3


def check_password(password, username):
    # These variables are local to this function
    has_min_length = len(password) >= 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    has_repeated_characters = False
    has_consecutive_numbers = False

    has_username = (
        bool(username)
        and username.lower() in password.lower()
    )

    # Check character types
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special_char = True

    # Check for adjacent repeated characters
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            has_repeated_characters = True
            break

    # Check for three ascending consecutive numbers
    for i in range(len(password) - 2):
        first = password[i]
        second = password[i + 1]
        third = password[i + 2]

        if first.isdigit() and second.isdigit() and third.isdigit():
            if int(first) + 1 == int(second) and int(second) + 1 == int(third):
                has_consecutive_numbers = True
                break

    # Return all the results in one dictionary
    return {
        "has_min_length": has_min_length,
        "has_uppercase": has_uppercase,
        "has_lowercase": has_lowercase,
        "has_digit": has_digit,
        "has_special_char": has_special_char,
        "has_username": has_username,
        "has_repeated_characters": has_repeated_characters,
        "has_consecutive_numbers": has_consecutive_numbers,
    }


def rank_password(checks):
    score = 0

    if checks["has_min_length"]:
        score += 1
    if checks["has_uppercase"]:
        score += 1
    if checks["has_lowercase"]:
        score += 1
    if checks["has_digit"]:
        score += 1
    if checks["has_special_char"]:
        score += 1
    if not checks["has_username"]:
        score += 1
    if not checks["has_repeated_characters"]:
        score += 1
    if not checks["has_consecutive_numbers"]:
        score += 1

    if score < 4:
        return PasswordStrength.WEAK
    elif score <= 6:
        return PasswordStrength.MODERATE
    else:
        return PasswordStrength.STRONG


def main():
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")

            checks = check_password(password, username)
            strength = rank_password(checks)

            print(f"Password strength: {strength.name}")


main()