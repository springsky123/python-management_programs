#FOOD DELIVERY PROGRAM

class customer:
    def __init__(self,customer_name,phone_no,email,address):
        self.customer_name = customer_name
        self.phone_no = phone_no
        self.email = email
        self.address = address
        self.order = []
    def place_order(self):
        while True:
            item_name = input("Enter item name(or 'done' to finish):")
            if item_name=='done':
                break
            elif item_name in menu:
                try:
                    quantity = input(f"Enter quantity of {item_name}:")
                    if quantity>0:
                       self.order.append((item_name,quantity,price))
                except ValueError:
                    print("Quantity must be positive.")
            else:
                print("Item not found.Please choose from the menu.")
    def cancel_order(self):
        pass
    def view_order(self):
        pass
    def order_history(self):
        pass
#main
name = input("Enter your name:")
phone_no = int(input("Enter your phone number(must be only 10 digit):"))
email = input("Enter your email:")
address = input("Enter your address:")
