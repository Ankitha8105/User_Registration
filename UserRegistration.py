'''
    @Author:Ankitha
    @Date: 21-11-2024
    @Last Modified by: Ankitha
    @Last Modified time: 21-11-2024
    @Title : User registration problem

'''
import re
import log as log

log = log.logger_init("registartionlogger")

def valid_firstname(fname):
    """
    Description:
        This function checks if user entered valid first name
    Parameter:
        fname: the name to be checked
    Returns:
        None
    """
    try :
        if (re.match('^[A-Z][a-z]{2,}$',fname)):
            log.info("First Name is valid")
            return True
        else:
            log.error("First Name is not valid ,please make sure first letter is capital and minimumof 3 letters")
            return False
    except Exception as e:
        log.error("Invalid! error in name")
        return False
    
def valid_lname(l_name):
    """
    Description:
        This function checks if user entered valid last name
    Parameter:
        l_name: the name to be checked
    Returns:
        None
    """
    try:
        if (re.match('^[A-Z][a-z]{2,}',l_name)):
            log.info("Valid Last name")
            return True
        else:
            log.info("Invalid !,please make sure first letter in upper case and minimum of 3 letters")
            return False
        
    except Exception as e:
        log.error("Some error occured")
        return False
    
def valid_email(email):
    """
    Description:
        This function checks if user entered valid email
    Parameter:
        email: the email to be checked
    Returns:
        None
    """
    try:
        if (re.match('^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$',email)):
            log.info("Valid Email")
            return True
        else:
            log.error("Invalid Email Please correct it")
            return False

    except Exception as e:
        log.error("Error occured")
        return False
    
def valid_mobilenum(mobile_num):
    """
    Description:
        This function checks if user entered valid Mobile Number
    Parameter:
        mobile_num: the mobile number to be checked
    Returns:
        None
    """
    try:
        if (re.match('^\d\d.\d{10}$',mobile_num)):
            log.info("Valid mobile number")
            return True
        else:
            log.error("Invalid! ,Please enter correct email")
            return False
    except Exception as e:
        log.error("Some Interruption is occured")

def main():
    first_name =input("Enter your First Name :")
    valid_firstname(first_name)
    last_name = input("Enter your last name :")
    valid_lname(last_name)
    email = input("Enter your Email :")
    valid_email(email)
    mobile_num = input("Enter valid mobile number :")
    valid_mobilenum(mobile_num)

if __name__ == "__main__":
    main()
    