#BANK ACCOUNT MANAGEMENT


import csv
from prettytable import PrettyTable

class bank_account:
    bank_name = "SBI"
    def __init__(self):
        self.name = "Bhawana"
        self.account_no = 235647890193
        self.branch_name = "Ranikhet"
        self.balance = 500
        self.display_info()
    #Instance method to display account holder info
    def display_info(self):
        print("........Bank account holder details........")
        print(f"Holder name:{self.name}")
        print(f"Account number:{self.account_no}")
        print(f"Branch name:{self.branch_name}")
        print(f"Bank balance:{self.balance}")
        print(f"Bank name:{bank_account.bank_name}")
    
    def deposit_amount(self):
        print("Your bank balance is",self.balance)
        amount = int(input("Enter amount for deposit:"))
        self.balance+=amount
        print("Your bank balance(after deposit)is",self.balance)
    def withdraw_amount(self):
        print("Your bank balance is",self.balance)
        amount = int(input("Enter amount for withdrawal:"))
        self.balance-=amount
        print("Your bank balance(after withdrawal)is",self.balance)
    def check_balance(self):
        print("Your bank balance :")
        print(self.balance)
    def transfer_amount(self):
        name = input("Enter reciver name:")
        account_no2 = int(input("Enter account number of reciver:"))
        amount = int(input("Enter amount to send :"))
        self.balance-=amount
        data = [name,account_no2,amount]
        #storing the above data in the csv file
        file = open("transfer_amount.csv",'a')
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()
    def show_transfer_detail(self):
        file = open("transfer_amount.csv",'r')
        read = csv.reader(file)
        next(read)
        table = PrettyTable()
        table.field_names = ['RECIVER_NAME','RECIVER_ACCOUNT_NUMBER','TRANSFERED_AMOUNT']
        for row in read:
            if row==[]:
                pass
            else:
                table.add_row(row)
        print(table)
    def calculate_interset(self):
        print("Your bank balance is",self.balance)
        print("After one year you got 2% interset:")
        print(self.balance*0.002)
        print("After getting interset your bank balance will be")
        print(self.balance*0.002+self.balance)
    #Function for options to choose 
    def choose_option(self):
        print('......................................')
        print('1.FOR DEPOSIT AMOUNT')
        print('2.FOR WITHDRAW AMOUNT')
        print('3.FOR CHECK BALANCE')
        print('4.FOR TRANSFER THE AMOUNT')
        print('5.FOR CALCULATE INTERSET ')
        print('6.FOR SHOW TRANFER DETAILS')
        print('7.FOR CLOSE ACCOUNT')
        print('.......................................')
        choose = int(input('enter your choice:'))
        return choose
    #Instance method to work on choice
    def choice_by_option(self):
        choice ='y'
        while choice=='y':
            opt = self.choose_option()
            if opt==1:
                self.deposit_amount()
            elif opt==2:
                self.withdraw_amount()
            elif opt==3:
                self.check_balance()
            elif opt==4:
                self.transfer_amount()
            elif opt==5:
                self.calculate_interset()
            elif opt==6:
                self.show_transfer_detail()
            elif opt==7:
                print("Closed account.........")
                break
            else:
                print('......invaild choice,please try again!..........')
            print()
            choice = input('>Do you want to continue?(type*y*for yes):')
#Create object of bank_account 
s = bank_account()
#call method
s.choice_by_option()
print("__________________")
print("-----------------THE END-----------------")
print()
