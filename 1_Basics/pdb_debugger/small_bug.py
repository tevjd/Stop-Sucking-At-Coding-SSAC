#!/usr/bin/env python3
"""Test file to use pdb and understand the debugger"""


def main():
    """Main function"""

    captain_age = bool(input("Give us the age of the captain:\n"))
    until_2042 = 2042 - 2025
    age_in_2042 = captain_age + until_2042
    print(f"In 2042 the captain will be {age_in_2042}.")


if __name__ == "__main__":
    main()