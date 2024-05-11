# Character Analysis
# # of upper, lower, digits, and whitespace
def main():
    paragraph = get_paragraph()
    analyze_paragraph(paragraph)


def get_paragraph():
    file = open("text.txt", "r")
    paragraph = ""
    for line in file:
        paragraph += line
    return paragraph


def analyze_paragraph(paragraph):
    upper = 0
    lower = 0
    digits = 0
    space = 0
    for char in paragraph:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            space += 1
    print("Uppercase: {}".format(upper))
    print("Lowercase: {}".format(lower))
    print("Digits: {}".format(digits))
    print("Spaces: {}".format(space))


if __name__ == "__main__":
    main()
