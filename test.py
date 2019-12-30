from fedora.client.fas2 import * 
from fedora.client import AuthError
import getpass 

fas = {}
def printfas(fuser):
    try:
        print("FAS Username: "+fuser['username'])
        print("FAS ID:"+str(fuser['id']))
        print("Email ID: "+fuser['email'])
        print("Bugzilla Email ID: "+fuser['bugzilla_email'])
        print("User's Real Name:"+fuser['human_name'])
    except:
        print("User does not exist! Please check Username")

def menu():
    while True:
        opt = input("Please select the option:\n1. Details by Username\n2. Details By FAS ID\nSelect:")
        if opt == "1":
            return "uname"
        elif opt == "2":
            return "fasid"
        else:
            print("Incorrect option!")

uname = input("Please enter your FAS Username:")
password = getpass.getpass("Please enter your FAS Password:")
sel = menu()
try:
    accsystem = AccountSystem(username=uname, password=password)
    if sel == "uname":
        name = input("Please enter the FAS Username in which you would like to get the details:")
        fas = accsystem.person_by_username(username=name)
    else:
        fasid = input("Please enter the FAS ID of the user you would like to get the details:")
        fas = accsystem.person_by_id(fasid)

except AuthError:
    print("Invalid Auth details! Please check user details and try again")
    exit(1)
except Exception as err:
    print("An error Occured")
    print(err)
    exit(1)
else:
    printfas(fas)

