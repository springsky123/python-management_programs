#FOOD DELIVERY PROGRAM

import random
from prettytable import PrettyTable

class customer:
    def __init__(self):
        self.order = []
        self.a_instance = Restaurant
    def place_order(self):
        menu = self.a_instance.display_menu()
        print(menu)
        print("----------SELECT ITEMS FORM MENU------------")
        while True:
            item_name = input("Enter item name(or 'done' to finish):")
            if item_name=='done':
                break
            elif item_name in menu:
                try:
                    quantity = input(f"Enter quantity of {item_name}:")
                    if quantity>0:
                        data = [item_name,quantity,price]
                        self.order.append(data)
                except ValueError:
                    print("Quantity must be positive.")
            else:
                print("Item not found.Please choose from the menu.")
        file.close()
    def cancel_order(self):
        pass
    def view_order(self):
        print("Your order list is:")
        table = PrettyTable()
        table.field_names = ['ITEM_NAME','QUANTITY','PRICE']
        for row in order:
            table.add_row(row)
        print(table)
    def order_history(self):
        pass
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
                self.order_history()
            else:
                print('......invaild choice,please try again!..........')
            print()    
            choice = input('>Do you want to continue?(type*y*for yes):')
class order:
    def __init__(self):
        self.status = {}
    def ordered_item:
        item = input("Enter item name:")
        amount = int(input("Enter the amount of item:"))
        status[item]=[amount]
    def total_price:
        pass
    def update_status:
        pass
class Restaurant:
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
