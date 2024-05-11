# Word frequency
# Create dictionary to accumulate word count

import string


def main():
    paragraph = get_paragraph()
    count_and_sort(paragraph)


def get_paragraph():
    # Create file object
    file = ""
    try:
        file = open("text.txt", "r")
    except FileNotFoundError:
        print("Error. No such file exists.")
    # Create placeholder variable to hold contents of file
    paragraph = ""
    for line in file:
        # Iterate over each line and concatenate it to the paragraph
        paragraph += line
    # Return the paragraph
    return paragraph


def count_and_sort(paragraph):
    # Read and sanitize the paragraph to remove whitespace and punctuation
    words = paragraph.upper()
    words = words.strip("\n")
    words = words.translate(str.maketrans('', '', string.punctuation))

    # Split the paragraph on the whitespaces
    words = words.split()
    # Calculate and display the number of items in the words list
    counter = {}
    for word in words:
        # If word already exists, add one to the counter
        if word in counter.keys():
            counter[word] += 1
        # If word does not exist, create word
        else:
            counter[word] = 1
    # Use lambda function to sort the items in the counter alphabetically by the key
    sorted_words = sorted(counter.items(), key=lambda x: x[0])
    # Open text file
    file = open("frequency.txt", "a")
    # Write each item in the sorted list to the file
    for item in sorted_words:
        item = list(item)
        file.write("{} : {}".format(item[0], item[1]))
        file.write("\n")


if __name__ == "__main__":
    main()
