# File encryption and decryption
# Write a program that uses a dictionary to assign codes to each letter.
# Open a text file, read contexts, encrypt to second file
# Open encrypted file and decrypt

def main():
    crypt_key = key_dict()
    # Pass code mapping dictionary to encrypting file
    encrypt(crypt_key)


def key_dict():
    # Create dictionary of code mapping
    keys = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "F", "F": "G", "G": "H", "H": "I", "I": "J", "J": "K",
            "K": "L", "L": "M", "M": "N", "N": "O", "O": "P", "P": "Q", "Q": "R", "R": "S", "S": "T", "T": "V",
            "V": "W", "W": "X", "X": "Y", "Y": "Z", "Z": "A", "a": "b", "b": "c", "c": "d", "d": "e", "e": "f",
            "f": "g", "g": "h", "h": "i", "i": "j", "j": "k", "k": "l", "l": "m", "m": "n", "n": "o", "o": "p",
            "p": "q", "q": "r", "r": "s", "s": "t", "t": "u", "u": "v", "v": "w", "w": "x", "x": "y", "y": "z",
            "z": "a"}
    # Return dictionary as a variable
    return keys


def encrypt(crypt_key):
    # Open text file
    file = open("9-3text.txt", "r")
    # Create placeholder sting for text
    text = ""
    # Add all text to string
    for line in file:
        text += line
    # Create placeholder string for encrypted text
    new_text = ""
    # Iterate over each character to encrypt according to code
    for char in text:
        # If space or newline character, copy
        if char.isspace():
            new_text += char
        else:
            # Use character as key to encrypt to new value
            char = crypt_key[char]
            new_text += char
    # Generate a new file
    new_file = open("encrypted.txt", "w")
    # Write encrypted text to file
    new_file.write(new_text)


if __name__ == "__main__":
    main()
