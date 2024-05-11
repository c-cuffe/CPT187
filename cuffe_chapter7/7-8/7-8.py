# Name Search. Read contents of files into separate lists. Enter name, determine if popular


def main():
    boy_names = boyNamesFile()
    girl_names = girlNamesFile()
    pop_name_test(boy_names, girl_names)


def boyNamesFile():
    # Generate a list that contains popular boys names
    file = open("BoyNames.txt", "r")
    pop_boy_names = []
    for line in file:
        line = line.strip("\n").lower()
        pop_boy_names.append(line)
    file.close()
    return pop_boy_names


def girlNamesFile():
    # Generate a list that contains popular girls names
    file = open("GirlNames.txt", "r")
    pop_girl_names = []
    for line in file:
        line = line.strip("\n").lower()
        pop_girl_names.append(line)
    file.close()
    return pop_girl_names


def pop_name_test(boys, girls):
    # Get a sample name from user
    while True:
        name = input("Enter a name: ").lower()
        if not name.isalpha():
            print("Error. Please enter a valid name.")
        else:
            break

    # Determine which list to compare to
    lists = ["boys", "girls", "both"]
    # Validate list choice
    while True:
        res = input("Would you like to search boys, girls, or both? ").lower()
        group = res
        if res not in lists:
            print("Error. Please make a valid entry")
        else:
            break

    # Determine if name is in list
    # Display result
    if group == "boys":
        if name in boys:
            print("That is a popular name for boys.")
        else:
            print("That is not a popular name for boys.")
    if group == "girls":
        if name in girls:
            print("That is a popular name for girls.")
        else:
            print("That is not a popular name for girls.")
    if group == "both":
        if name in girls and name in boys:
            print("That is a popular name for boys and girls.")
        elif name in girls:
            print("That is a popular name for girls, not boys.")
        elif name in boys:
            print("That is a popular name for boys, not girls.")
        elif name not in boys and name not in girls:
            print("That is not a popular name for boys or girls.")


if __name__ == "__main__":
    main()
