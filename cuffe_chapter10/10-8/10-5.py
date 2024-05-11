# Create RetailItem class
class RetailItem:
    # Take in attributes
    def __init__(self, item, units, price):
        self.__item = item
        self.__units = units
        self.__price = price

    # Create mutators
    def set_description(self, item):
        if item.isalpha():
            self.__item = item

    def set_units(self, units):
        if units.isnumeric():
            self.__units = units

    def set_price(self, price):
        try:
            float(price)
            self.__price = price
        except:
            self.__price = 0

    # Create accessors
    def get_item(self):
        return self.__item

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price


def main():
    # Create three instances
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)
    # Create table to display info
    print("\t\t\tDescription\tUnits in Inventory\tPrice")
    print("Item #1\t\t{}\t\t\t{}\t\t\t\t{}".format(item1.get_item(), item1.get_units(), item1.get_price()))
    print("Item #2\t\t{}\t{}\t\t\t\t{}".format(item2.get_item(), item2.get_units(), item2.get_price()))
    print("Item #3\t\t{}\t\t\t{}\t\t\t\t{}".format(item3.get_item(), item3.get_units(), item3.get_price()))


if __name__ == "__main__":
    main()
