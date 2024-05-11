# Import 10-5 as the variable retail
retail = __import__("10-5")


# Create CashRegister class
class CashRegister:
    # Create empty list to hold cart items
    def __init__(self):
        self.items = []

    # Add items to cart
    def purchase_item(self, item):
        self.items.append(item)

    # For each item in the cart, add the price to the total
    def get_total(self):
        # Set total accumulator
        total = 0
        # Get price from stored item
        for item in self.items:
            total += item.get_price()
        # Display the total
        print("{:.2f}".format(total))

    # For each item in the cart, display item attributes
    def show_items(self):
        for item in self.items:
            # Get item information from stored item
            print("Item:", item.get_item())
            print("Units:", item.get_units())
            print("Price:", item.get_price())
            print("")

    # Empty list contents
    def clear(self):
        self.items = []


def main():
    # Create three instances of imported RetailItem class
    item1 = retail.RetailItem("Jacket", 12, 59.95)
    item2 = retail.RetailItem("Designer Jeans", 40, 34.95)
    item3 = retail.RetailItem("Shirt", 20, 24.95)

    # Create variable for easy class access
    register = CashRegister()

    # Create infinite loop while items are continuing to be purchased
    cart_open = True
    while cart_open:
        # Select and perform corresponding action
        print("Select an action: ")
        print("1. Add an item to the cart")
        print("2. Checkout")
        print("3. Clear cart")
        print("4. Quit")
        choice = input("")
        if choice == "1":
            # Select item and pass to the purchase_item method in CashRegister class
            print("Select an item:")
            print("1. Jacket")
            print("2. Designer Jeans")
            print("3. Shirt")
            item = input("")
            if item == "1":
                register.purchase_item(item1)
            elif item == "2":
                register.purchase_item(item2)
            elif item == "3":
                register.purchase_item(item3)
            else:
                print("Error. Invalid selection.")
        elif choice == "2":
            print("Total:")
            register.get_total()
            print("Items in Cart:")
            register.show_items()
        elif choice == "3":
            register.clear()
        # If they quit program, break loop
        elif choice == "4":
            cart_open = False
        else:
            print("Error. Invalid selection.")


if __name__ == "__main__":
    main()
