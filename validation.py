from datetime import *
import re 
def validname(name):
    l=name.split()
    if len(l)==3:
        if l[0].isalpha() and l[1].isalpha() and l[2].isalpha():
            return True
    return False
    
def validmobno(mobno):
    if len(mobno)==10 and mobno.isdigit() and mobno[0] == '6' or mobno[0]=='7' or mobno[0]=='8' or mobno[0]=='9':
        return True
    else:
        return False
 
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def validadhar(adharno):
    if len(adharno)==12 and adharno.isdigit():
        return True
    else:
        return False

def validpan(pan): 
    exp="^[A-Za-z]{5}\d{4}[A-Za-z]{1}$"
    if re.match(exp,pan):
        return True
    else:
        return False
import re
def validIFSCCode(ifsc):
    exp = "^[A-Z]{4}0[A-Z0-9]{6}$"
    if re.match(exp,ifsc):
        return True
    else:
        return False

def validbankaccnum(accnum):
    exp="^[0-9]{9,18}$"
    if re.match(exp,accnum):
        return True
    else:
        return False

def validGender(gen):
    exp="(?:male|Male|MALE|female|Female|FEMALE)$"
    if re.match(exp,gen):
        return True
    else:
        return False


def validate_account_type(account_type):
    valid_account_types = ['savings', 'current', 'joint']
    a=account_type.lower()
    if a in valid_account_types:
        return True
    else:
        return False

def validate_dob(date_text):
    try:
        dob = datetime.strptime(date_text, '%Y-%m-%d')
        year, month, day = dob.year, dob.month, dob.day

        if month > 12 or day > 31:
            return False

        thirty_days_month = [4, 6, 9, 11]  # April, June, September, November
        if month in thirty_days_month and day > 30:
            return False

        february = 2
        if month == february:
            if day > 29:
                return False
            leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
            if not leap_year and day > 28:
                return False

        return True

    except ValueError:
        return False

def calculate_age(date_text):
    if validate_dob(date_text):
        dob = datetime.strptime(date_text, '%Y-%m-%d')
        today = datetime.today()

        years = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            years -= 1

        return years

    else:
        return None

# Example usage
#date_of_birth = input()

'''if validate_dob(date_of_birth):
    3age = calculate_age(date_of_birth)
    f age <18:
        print("cannot create bank account. Age should be greater than 18")
    elif age is not None:
        print(f"The person's age is {age} years.")
    else:
        print("Invalid date of birth.")
else:
    print("Invalid date of birth.")'''


def validcity(state,city):
    sc={"Maharashtra":['Mumbai','Pune','Nashik'],'AndhraPradesh':['Guntur','Warangal','Vijayawada'],'Karnataka':['Mysore','Bangalore']}
    key=sc.keys()
    if state in key:
        v=sc[state]
        if city in v:
            return True
        else:
            return False
    else:
        return False

def validaddress(address):
    if len(address)>=5 and len(address)<=200:
        return True
    else:
        return False








