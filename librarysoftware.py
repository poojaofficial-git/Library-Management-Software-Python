"""PROGRAM TO KEEP RECORD OF STUDENTS ISSUING LIBRARY BOOKS OF USHA MITTAL INSTITUTE OF TECHNOLOGY"""

import os
def enter_choice():
    print('****************WELCOME TO USHA MITTAL INSTITUTE OF TECHNOLOGY LIBRARY*******************')
    print('---------------------Enter choice----------------------')
    print("1.create student account\n2.view the account\n3.Issue and Return date\n4.Extend return date\n5.To Recieve Book\n6.Delete account\n 0.To Exit")
    num=int(input("Enter your choice:"))
    if num==1:
        create_account()
    elif num==2:
        view_account()
    elif num==3:
        append_file()
    elif num==4:
        append_file2()
    elif num==5:
        submitted()
    elif num==6:
        delete()
  
    elif num==0:
        print("---------------------Thank you-------------------")
    else:
        print("------------error try again---------------------")
        enter_choice()
def create_account():
    print('---------------------student account----------------------')
    stud_id=input("Enter student ID\n")
    name=input("Enter the student name:\n")
    branch=input("Enter students branch:\n")
    year=input("student's year:\n")
    mobile_no=input("students mobile number:\n")

    with open(stud_id,'w')as output_file:
        output_file.write("ID:"+stud_id+"\nName:"+name+"\nBranch:"+branch+"\nMobile:"+mobile_no+"\nYear:"+year)
    print("Student",stud_id,"is created")
    enter_choice()

def view_account():
    print('---------------------Students Profile Information----------------------')
    stud_id=input("Enter Students ID:")
    with open(stud_id,'r')as open_file:
        contents=open_file.read()
        print(contents)
        open_file.close()
    enter_choice()

def append_file():
    print('---------------------Issue And Return Date----------------------')
    stud_id=input("Enter stud ID\n")
    book_no=input("Enter book number:\n")
    issue_date=input("Enter issue dated(dd/mm/yyyy):\n")
    return_date=input("Enter return date(dd/mm/yyyy):\n")
    with open(stud_id,'a')as output_file:
        output_file.write("\n\nID:"+stud_id+"\nBook_Number:"+book_no+"\nIssue_date:"+issue_date+"\nReturn_date:"+return_date)
    print("Student",stud_id,"has issued",book_no,"book")
    print('---------------------------------------------------------------------------------')
    enter_choice()
    
def append_file2():
    print('---------------------Extend Return Date----------------------')
    stud_id=input("Enter stud ID\n")
    book_no=input("Enter book number:\n")
    new_return_date=input("Enter return date u want to extend(dd/mm/yyyy):\n")
    with open(stud_id,'a')as output_file:
        output_file.write("\n\nID:"+stud_id+"\nBook_Number:"+book_no+"\nnew_return_date:"+new_return_date)
    print("Student",stud_id,"has issued",book_no,"book again")
    enter_choice()

def submitted():
    
    stud_id=input("Enter stud ID:\n")
    import time
    current_date=time.strftime("%d/%m/%y")
    return_date=input('enter the return date:')
    print('current date:',current_date)
    print('return_date:',return_date)
    
    if (return_date>current_date):
        print('book has been returned b4 due date')
        
    elif (current_date==return_date):
        print('book returned on time')
        
    else:
        deposit=int(input('enter you deposit:'))
        print('U have not returned the book on time:')
        n=int(input("enter number of days after which book is received - "))
        fine = (n)*2
        bal = deposit - fine
        print("deposit-",deposit,"Rs")
        print("fine - ",fine,"Rs")
        print("available balance - ",bal,"Rs")
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    enter_choice()
    
    
    
def delete():
    filename=input("Enter Students ID to delete:")
    if os.path.exists(filename):
        os.remove(filename)
        print("Report",filename,"deleted")
    else:
        print("sorry,I can not find %s report."%filename)       
    enter_choice()


    
enter_choice()
