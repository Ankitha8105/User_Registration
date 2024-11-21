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

def main():
    first_name =input("Enter your First Name :")
    valid_firstname(first_name)
      
if __name__ == "__main__":
    main()
    