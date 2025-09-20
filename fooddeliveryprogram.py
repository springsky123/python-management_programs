import random

class Customer:
    """Represents a customer who can place and manage food orders."""
    def __init__(self, name):
        self.name = name  # Customer's name
        self.current_order = None  # Active order (if any)
        self.order_history = []  # List of past orders

    def place_order(self, restaurant):
        """Allow the customer to place a new order if no active order exists."""
        if self.current_order:
            print("You already have an active order. Please cancel it first.")
            return

        order = Order()
        restaurant.display_menu()  # Show menu before ordering

        while True:
            try:
                item_id = int(input("Enter item ID to add (0 to finish): "))
                if item_id == 0:
                    break
                if item_id not in restaurant.menu:
                    print("Invalid item ID.")
                    continue
                quantity = int(input("Enter quantity: "))
                item = restaurant.menu[item_id]
                order.add_item(item["name"], item["price"], quantity)
            except ValueError:
                print("Please enter valid numbers.")

        if order.items:
            self.current_order = order
            self.order_history.append(order)
            print("Order placed successfully.")
        else:
            print("No items were added. Order not placed.")

    def cancel_order(self):
        """Cancel the active order if there is one."""
        if self.current_order:
            print("Order cancelled.")
            self.current_order = None
        else:
            print("No active order to cancel.")

    def view_order(self):
        """Display the current active order details."""
        if self.current_order:
            print(f"\nCurrent Order (Status: {self.current_order.status}):")
            self.current_order.show_ordered_items()
        else:
            print("No active order.")

    def view_order_history(self):
        """Show all past orders for the customer."""
        print(f"\nOrder History of {self.name}:")
        if not self.order_history:
            print("No past orders.")
            return
        for i, order in enumerate(self.order_history, 1):
            print(f"\nOrder #{i} - Status: {order.status}")
            order.show_ordered_items()

    def options(self):
        """Display menu options for customer actions and get the user's choice."""
        print('--------------------------------------')
        print('1. Place order')
        print('2. Cancel order')
        print('3. View order')
        print('4. See order history')
        print('--------------------------------------')
        while True:
            try:
                option = int(input('Enter your choice: '))
                return option
            except ValueError:
                print("Please enter a valid number.")

    def choice_by_option(self, restaurant):
        """Loop for user to select actions until they choose to exit."""
        choice = 'y'
        while choice.lower() == 'y':
            opt = self.options()
            if opt == 1:
                self.place_order(restaurant)
            elif opt == 2:
                self.cancel_order()
            elif opt == 3:
                self.view_order()
            elif opt == 4:
                self.view_order_history()
            else:
                print('Invalid choice, please try again!')
            print()
            choice = input('Do you want to continue? (type "y" for yes): ')

class Order:
    """Represents a food order with multiple items."""
    def __init__(self):
        self.items = []  # List of items in the order
        self.status = "Pending"  # Order status

    def add_item(self, name, price, quantity):
        """Add an item to the order."""
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def show_ordered_items(self):
        """Display all ordered items and the total price."""
        if not self.items:
            print("No items in this order.")
            return
        total = 0
        for item in self.items:
            print(f"{item['name']} x{item['quantity']} @ ${item['price']} each")
            total += item['price'] * item['quantity']
        print(f"Total: ${total:.2f}")

class Restaurant:
    """Restaurant with a menu of available food items."""
    def __init__(self):
        self.app_name = "Fastfood"
        # Menu is a dictionary mapping item_id to item details
        self.menu = {
            1: {"name": "Burger", "price": 5.0},
            2: {"name": "Fries", "price": 2.5},
            3: {"name": "Soda", "price": 1.5}
        }

    def display_menu(self):
        """Print the current menu to the screen."""
        print("\nMenu:")
        for item_id, details in self.menu.items():
            print(f"{item_id}: {details['name']} - ${details['price']}")

def sign_up():
    """Sign-up flow for a new customer, including basic validation and OTP simulation."""
    while True:
        phone_no = input("Enter your phone number (must be 10 digits): ")
        if len(phone_no) == 10 and phone_no.isdigit():
            break
        print("Invalid phone number. Please enter exactly 10 digits.")
    print("OTP FOR VERIFICATION:", random.randrange(1000, 9999))
    address = input("Enter your address: ")
    name = input("Enter your name: ")
    cus = Customer(name)
    rest = Restaurant()
    cus.choice_by_option(rest)

if __name__ == "__main__":
    sign_up()
