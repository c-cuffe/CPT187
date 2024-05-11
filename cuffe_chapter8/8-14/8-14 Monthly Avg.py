def main():
    info = get_info()
    monthly_avg(info)


def get_info():
    file = open("GasPrices.txt", "r")
    info = []
    for line in file:
        ind_info = []
        line = line.strip("\n")
        data = line.split(":")
        dates = data[0].split("-")
        ind_info.append(dates[0])  # month
        ind_info.append(dates[1])  # day
        ind_info.append(dates[2])  # year
        ind_info.append(data[1])  # price
        info.append(ind_info)
    return info


def monthly_avg(info):
    # Create parallel list of month names
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    # Set variable for loop iterable
    entries = len(info)
    # Create loop to iterate through each month
    for m in range(12):
        month = m + 1
        # Set accumulator values for number of prices and total prices
        monthly_total = 0
        prices = 0
        for item in range(entries):
            # Pass if month does not correspond
            if int(info[item][0]) != month:
                pass
            else:
                # Add price to accumulators
                monthly_total += float(info[item][3])
                prices += 1
        # Calculate average
        average = monthly_total / prices
        # Display average and corresponding month name
        print("Month: {} | Average: ${:.3f}".format(months[m], average))


if __name__ == "__main__":
    main()
