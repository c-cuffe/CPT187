def main():
    crypt_key = key_dict()
    #Pass code mapping dictionary to decrypting file
    decrypt(crypt_key)

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


def decrypt(crypt_key):
    # Open encrypted file
    file = open("encrypted.txt", "r")
    # Generate placeholder string for text
    text = ""
    # Copy each line to string
    for line in file:
        text += line
    new_text = ""
    # Create a list of all items in the code dictionary
    items = crypt_key.items()
    # Iterate over each character
    for char in text:
        # If space or newline character, copy
        if char.isspace():
            new_text += char
        else:
            # Generate a list of keys
            keys = list(crypt_key.keys())
            # Generate the list of values
            values = list(crypt_key.values())
            # Determine the index of the character in values
            index = values.index(char)
            # Use values index to find associated key
            char = keys[index]
            # Copy decrypted character to string
            new_text += char
    # Print the decrypted text
    print(new_text)

if __name__ == "__main__":
    main()
