import random


# Write a program that simulates a magic 8-ball. Use file. Ask question, display random response.
def main():
    magic_8_ball = ball_responses()
    ask_question(magic_8_ball)
    go_again()


def ball_responses():
    # Create a list that contains the 8-ball responses
    file = open("8_ball_responses.txt", "r")
    responses = file.readlines()
    return responses


def ask_question(magic_8_ball):
    question = input("Ask a question: ")
    # Generate a random number
    response = random.randint(1, 12)
    # Assign number to list index
    answer = magic_8_ball[response]
    # Print response
    print(answer)


def go_again():
    again = input("Would you like to ask another question? Y/N ").lower()
    if again == "y":
        main()
    else:
        exit()


if __name__ == "__main__":
    main()
