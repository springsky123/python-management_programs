#FOOD DELIVERY PROGRAM

import random

class customer:
    def __init__(self):
        self.current_order = None
        self.order_history = []

    def place_order(self, restaurant):
        if self.current_order:
            print("You already have an active order. Please cancel it first.")
            return

        order = Order()
        restaurant.display_menu()

        while True:
            try:
                item_id = int(input("Enter item ID to add (0 to finish): "))
                if item_id == 0:
                    break
                if item_id not in restaurant.menu:
                    print(" Invalid item ID.")
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
            print(" No items were added. Order not placed.")

    def cancel_order(self):
        if self.current_order:
            print("Order cancelled.")
            self.current_order = None
        else:
            print("No active order to cancel.")

    def view_order(self):
        if self.current_order:
            print(f"\n Current Order (Status: {self.current_order.status}):")
            self.current_order.show_ordered_items()
        else:
            print(" No active order.")

    def view_order_history(self):
        print(f"\n Order History of {self.name}:")
        if not self.order_history:
            print("No past orders.")
            return
        for i, order in enumerate(self.order_history, 1):
            print(f"\n Order #{i} - Status: {order.status}")
            order.show_ordered_items()
    #function for options to choose 
    def options(self):
        print('......................................')
        print('1.For place order ')
        print('2.For cancel order ')
        print('3.For view order')
        print('4.For see order history')
        print('.......................................')
        option = int(input('enter your choice:'))
        return option
    #Instance method to work on choice
    def choice_by_option(self):
        choice ='y'
        while choice=='y':
            opt = self.options()
            if opt==1:
                self.place_order()
            elif opt==2:
                self.cancel_order()
            elif opt==3:
                self.view_order()
            elif opt==4:
                self.view_order_history()
            else:
                print('......invaild choice,please try again!..........')
            print()    
            choice = input('>Do you want to continue?(type*y*for yes):')
class order:
    def __init__(self):
        self.status = {}
    def ordered_item(self):
        item = input("Enter item name:")
        amount = int(input("Enter the amount of item:"))
        status[item]=[amount]
    def total_price(self):
        pass
    def update_status(self):
        pass
class restaurant:
    def __init__(self):
        self.app_name = "Fastfood"
    def display_menu(self):
        pass
    def remove_item(self):
        pass
    def add_item(self):
        pass
#function for log_in or sign_up
def sign_up():
    phone_no = int(input("Enter your phone number(must be only 10 digit):"))
    print("OTP FOR VERIFICATON:",random.randrange(1000,9999))
    address = input("Enter your address:")
    #create object of customer
    cus = customer()
    #call method
    cus.choice_by_option()
#call function
sign_up()
