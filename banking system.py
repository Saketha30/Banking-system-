import random
from validation import *
class BankAccount:
    def __init__(self,Bankname,IFSCcode,Accountnumber,Accountholdername,Age,Gender,DOB,Address,State,City,Typeofaccount,Balance,Pannumber,Aadharnumber,Mobilenumber):
        self.Bankname=Bankname
        self.IFSCcode=IFSCcode
        self.Accountnumber=Accountnumber
        self.Accountholdername=Accountholdername
        self.Age=Age
        self.Gender=Gender
        self.DOB=DOB
        self.Address=Address
        self.State=State
        self.City=City
        self.Typeofaccount=Typeofaccount
        self.Balance=Balance
        self.Pannumber=Pannumber
        self.Aadharnumber=Aadharnumber
        self.Mobilenumber=Mobilenumber
    def display(self):
        print(self.Bankname," ",self.IFSCcode," ",self.Accountnumber," ",self.Accountholdername," ",self.Age," ",self.Gender," ",self.DOB," ",self.Address," ",self.City," ",self.Typeofaccount," ",self.Balance," ",self.Pannumber," ",self.Aadharnumber," ",self.Mobilenumber)

bank=[]
while True:
    print("1:Add a record ")
    print("2:Display the  records ")
    print("3:search")
    print("4:Update")
    print("5:Delete")
    print("6:Deposit")
    print("7:withdrawl")
    print("8:Exit")
    choice=int(input("Enter choice "))
    if choice==1:
        Bankname=input("Enter name of the Bank: ")
        while True:
            IFSCcode=input("Enter IFSC code of your bank: ")
            if validIFSCCode(IFSCcode):
                break
            else:
                print("Invalid")
        '''while True:
            Accountnumber=(input("Enter acc number: "))
            if validbankaccnum(Accountnumber):
                break
            else:
                print("Invalid")'''
        def generate_bank_account_number():
            Accountnumber = ''.join([str(random.randint(0, 9)) for i in range(10)])
            return Accountnumber
        Accountnumber = generate_bank_account_number()
        print("Your Account Number:", Accountnumber)
        while True:
            Accountholdername=input("Enter name: ")
            if validname(Accountholdername):
                break
            else:
                print("Invalid name")
        Age=int(input("Enter age: "))
        while True:
            Gender=input("Enter your gender: ")
            if validGender(Gender):
                break
            else:
                print("Invalid")
        while True:
            DOB=input("Enter your dob in yyyy-mm-dd format: ")
            if validate_dob(DOB):
                break
            else:
                print("Invalid")
        while True:
            Address=input("Enter your address: ")
            if validaddress(Address):
                break
            else:
                print("Invalid")
        while True:
            State=input("Enter State: ")
            City=input("Enter city: ")
            if validcity(State,City):
                break
            else:
                print("Invalid")
        while True:
            Typeofaccount=input("Enter type of account: ")
            if validate_account_type(Typeofaccount):
                break
            else:
                print("Invalid")
        Balance=int(input("Enter balance: "))
        while True:
            Pannumber=input("Enter pan: ")
            if validpan(Pannumber):
                break
            else:
                print("Invalid")
        while True:
            Aadharnumber=(input("Enter aadhar: "))
            if validadhar(Aadharnumber):
                break
            else:
                print("Invalid")
        while True:
            Mobilenumber=input("Enter mob no: ")
            if validmobno(Mobilenumber):
                break
            else:
                print("Invalid")
            
        b=BankAccount(Bankname,IFSCcode,Accountnumber,Accountholdername,Age,Gender,DOB,Address,State,City,Typeofaccount,Balance,Pannumber,Aadharnumber,Mobilenumber) 
        bank.append(b)
    elif choice==2:
        print("Details of BankAccount: ")
        for i in bank:
            i.display()
    
    elif choice==3:
        print("Press A to search by account number: ")
        print("Press B to search by name: ")
        print("Press C to search by Type of account: ")
        ch=input("Enter choice: ")
        if ch=="A":
            accnum=(input("Enter account number to search: "))
            for i in bank:
                if i.Accountnumber==accnum:
                    i.display()
        elif ch=="B":
            nm=input("Enter name to search: ")
            for i in bank:
                if i.Accountholdername==nm:
                    i.display()
        elif ch=="C":
            acc=input("Enter type of account to search: ")
            for i in bank:
                if i.Typeofaccount==acc:
                    i.display()
    elif choice==4:
        accnum=(input("Enter your account number: "))
        for i in bank:
            if i.Accountnumber==accnum:
                print("press I to update name: ")
                print("press II to update address: ")
                print("press III to update DOB: ")
                ch=input("Enter choice: ")
                if ch=="I":
                    nm=input("Enter your new name: ")
                    i.Accountholdername=nm
                elif ch=="II":
                    add=input("Enter new address: ")
                    i.Address=add
                elif ch=="III":
                    db=input("Enter dob: ")
                    i.DOB=db
                else:
                    print("Invalid")
    elif choice==5:
        accnum=(input("Enter Account number: "))
        for i in bank:
            if i.Accountnumber==accnum:
                bank.remove(i)
    elif choice==6:
        accnum=(input("Enter account number: "))
        for i in bank:
            if i.Accountnumber==accnum:
                amount=int(input("Enter amount to deposit: "))
                i.Balance=i.Balance+amount
    elif choice==7:
        accnum=(input("Enter account number: "))
        for i in bank:
            if i.Accountnumber==accnum:
                amount=int(input("Enter amount to withdrawl: "))
                i.Balance=i.Balance-amount
                
    elif choice==8:
        break
    else:
        print("Invalid")
        
