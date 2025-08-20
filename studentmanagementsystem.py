#STUDENT DETAIL MANAGEMENT SYSTEM

import csv
from prettytable import PrettyTable

class student:
    college_name = 'IIT'
    #Constructor(Initializer method)
    def __init__(self,name,roll,age,address,marks):
        self.name = name
        self.roll = roll
        self.age = age
        self.address = address
        self.marks = marks
    #Instance method to display student info
    def display_info(self):
        print("...............")
        print(f"Student name:{self.name}")
        print(f"Roll number:{self.roll}")
        print(f"Age:{self.age}")
        print(f"Address:{self.address}")
        print(f"Marks:{self.marks}")
        print(f"College name:{student.college_name}")
    #Instance method to check result by marks
    def check_result(self):
        if 100>=self.marks>=85:
            print("Result:Pass,Got Grade A")
        elif 85>self.marks>=60:
            print("Result:Pass,Got Grade B")
        elif 60>self.marks>=50:
            print("Result:Pass,Got Grade C")
        elif 50>self.marks>=40:
            print("Result:Pass,Got Grade D")
        else:
            print("Result:Fail")
    #Instance method to save student info in csv file
    def save_info(self):
        data = [self.name,self.roll,self.age,self.address,self.marks,student.college_name]
        #storing the above data in the csv file
        file = open('studentrecord.csv','a')
        writer = csv.writer(file)
        writer.writerow(data)
        print()
        print(">>>Student record added successfully")
        file.close()
    #function for options to choose 
    def options(self):
        print('......................................')
        print('1.For display student record')
        print('2.For check result ')
        print('3.For save student record')
        print('.......................................')
        option = int(input('enter your choice:'))
        return option
    #Instance method to work on choice
    def choice_by_option(self):
        choice ='y'
        while choice=='y':
            opt = self.options()
            if opt==1:
                self.display_info()
            elif opt==2:
                self.check_result()
            elif opt==3:
                self.save_info()
            else:
                print('......invaild choice,please try again!..........')
            print()    
            choice = input('>Do you want to continue?(type*y*for yes):')
#Instance method to show all students info
def show_data():
    file = open('studentrecord.csv','r')
    read = csv.reader(file)
    next(read)
    table = PrettyTable()
    table.field_names = ['NAME','ROLL_NUMBER','AGE','ADDRESS','MARKS','COLLEGE_NAME']
    for row in read:
        if row==[]:
            pass
        else:
            table.add_row(row)
    print(table)
#Instance method to input student details by user
def input_info():
    n = int(input("Enter range:"))
    while n>0:
        print("Please enter student details..........")
        name = input("Enter student name:")
        roll = input("Enter student roll no:")
        age = int(input("Enter student age:"))
        address = input("Enter student address:")
        marks  = int(input("Enter students marks:"))
        print()
        #Create object of student 
        s = student(name,roll,age,address,marks)
        #call method
        s.choice_by_option()
        print("__________________")
        print()
        n-=1
    main()
#function for options to choose 
def choose_option():
    print('......................................')
    print('1.For input student record')
    print('2.For print all student record')
    print('.......................................')
    choose = int(input('enter your choice:'))
    return choose
#Function to handle the entireprogram
def main():
    choice ='y'
    while choice=='y':
        opt = choose_option()
        if opt==1:
            input_info()
        elif opt==2:
            show_data()
        else:
            print('......invaild choice,please try again!..........')
        print()
        choice = input('>Do you want to continue?(type*y*for yes):')
#call function
main()
print("______________The End______________")
        

