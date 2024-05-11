START_YEAR = 1993
END_YEAR = 2013
def main():
    info = get_info()
    annual_min_max(info)


def annual_min_max(info):
    # Create parallel list with month names
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    entries = len(info)
    for year in range(START_YEAR, END_YEAR + 1):
        prices = []
        months = []
        days = []
        for item in range(entries):
            if info[item][2] == str(year):
                price = float(info[item][3])
                prices.append(price)
                months.append(int(info[item][0]))
                days.append(int(info[item][1]))
        lowest_price = prices.index(min(prices))
        min_month = months[lowest_price]
        min_day = days[lowest_price]
        min_month_name = month_names[min_month - 1]
        highest_price = prices.index(max(prices))
        max_month = months[highest_price]
        max_day = days[highest_price]
        max_month_name = month_names[max_month - 1]
        print("Year: {} | Lowest price: {} {} ${:.3f} | Highest price: {} {} ${:.3f}".
              format(year, min_month_name, min_day, min(prices), max_month_name, max_day, max(prices)))
        prices = []
        months = []
        days = []


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


if __name__ == "__main__":
    main()
