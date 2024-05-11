# Write a program that reads file into a list. Enter account number.
# Determine if number is valid. If valid, display message.
# If not valid, display message


def main():
    accounts = account_nums()
    validate_account(accounts)


def account_nums():
    # Compile lines in file to a list
    file = open("charge_accounts.txt", "r")
    acc_nums = str(file.readlines())
    file.close()
    return acc_nums


def validate_account(accounts):
    # Determine if user inputted account is in the list
    # Display result
    while True:
        test = input("Enter a 7-digit account number: ")
        if not test.isnumeric() or len(test) != 7:
            print("Error. Please enter a 7-digit number.")
        else:
            test = str(test)
            break
    if test in accounts:
        print("This is a valid account.")
    else:
        print("This is not a valid account.")


if __name__ == "__main__":
    main()
