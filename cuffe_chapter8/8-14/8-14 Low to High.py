def main():
    info = get_info()
    asc_prices(info)


def asc_prices(info):
    # Generate file
    file = open("AscendingPrices.txt", "w")
    # Create variable for loop iterable
    entries = len(info)
    # Create empty lists for prices, sorted prices, and the dates
    prices = []
    prices_sorted = []
    dates = []
    for item in range(entries):
        # For each item, add the date and price to both lists
        prices.append(str(info[item][1]))
        prices_sorted.append((str(info[item][1])))
        dates.append(info[item][0])
    # Sort secondary list
    prices_sorted.sort()
    for item in range(len(prices_sorted)):
        # Save price
        price = float(prices_sorted[item])
        # Find date using corresponding index with original price list
        date = dates[prices.index(prices_sorted[item])]
        # Print the date and price
        file.write("Date: {} | Price: ${:.3f}".format(date, price))
        # Add a newline character at the end of each entry
        file.write("\n")
    file.close()


def get_info():
    # Read in and sanitize data from file into a list
    file = open("GasPrices.txt", "r")
    info = []
    for line in file:
        ind_info = []
        line = line.strip("\n")
        data = line.split(":")
        ind_info.append(data[0])  # date
        ind_info.append(data[1])  # price
        # Append date and price to info list
        info.append(ind_info)
    file.close()
    return info


if __name__ == "__main__":
    main()
