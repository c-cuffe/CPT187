# Annual Averages
START_YEAR = 1993
END_YEAR = 2013
def main():
    # Call function to get data from file
    info = get_info()
    # Call function to determine annual averages
    avg_annual(info)


def avg_annual(info):
    # Set variable for loop range to iterate over each entry in list
    entries = len(info)
    # Creat loop to iterate over each year
    for year in range(START_YEAR, END_YEAR + 1):
        # Set accumulators for total yearly price and number of prices per year
        prices = 0
        annual_total = 0
        # Iterate over each entry
        for item in range(entries):
            if info[item][0] == str(year):
                # Add corresponding prices to accumulators
                annual_total += float(info[item][1])
                prices += 1
        # Calculate and print average
        print("Year: {} | Average price: ${:.3f}".format(year,(annual_total/prices)))
        # Reset accumulators after each iteration
        annual_total = 0
        prices = 0


def get_info():
    # Create file object
    file = open("GasPrices.txt", "r")
    # Create empty list
    info = []
    for line in file:
        ind_info = []
        # Sanitize and separate data in each line
        line = line.strip("\n")
        data = line.split(":")
        dates = data[0].split("-")
        # Append necessary data to list
        ind_info.append(dates[2])  # year
        ind_info.append(data[1])  # price
        info.append(ind_info)
    # Return list to main function
    file.close()
    return info


if __name__ == "__main__":
    main()
