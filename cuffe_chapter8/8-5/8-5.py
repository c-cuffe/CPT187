# Alphabetic Telephone Number Translator


def main():
    number = validate_number()
    num_trans(number)


def validate_number():
    while True:
        # Get number from user and validate
        number = input("Enter a phone number in XXX-XXX-XXXX format: ")
        if len(number) == 12:
            for c in number:
                if c in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "-"] or c.isalpha():
                    pass
                else:
                    break
            # Return validated number to main
            return number
        else:
            print("Error. Please enter a valid number.")


def num_trans(number):
    # List of alphanumeric mappings
    alpha = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"],
             ["M", "N", "O"], ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]]
    # Placeholder for new phone number
    new_number = ""
    for digit in number:
        # Passes values that are numeric or dash
        if digit.isnumeric() or digit == "-":
            new_number += digit
        elif digit.isalpha():
            # Compares letter to values in alphanumeric mapping
            for num in range(len(alpha)):
                if digit in alpha[num]:
                    new_digit = str((num + 2))
                    # Concatenates numeric value to number
                    new_number += new_digit
    # Prints new number
    print(new_number)


if __name__ == "__main__":
    main()
