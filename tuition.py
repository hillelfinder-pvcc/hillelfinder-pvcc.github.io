#Name: Hillel Finder
#Name: Ethan Mallon
#Prog Purpose: the program comuters PVCC college tuition & fees based on number of credits
#   PVCC FEE Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
#define tution & fee rates (per credit)
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1 #1 means in-state, 2 means out-of-state
numcredits = 0
scholarship = 0

tuition_type = 0
full_tut = 0
full_cap = 0
full_inst = 0
full_act = 0
total = 0
balance = 0

##define program functions
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        if inout == 1 or inout == 2:
            display_results()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.upper() == "N" or yesno.upper() == "NO":
            print("Thanks for stopping by!")
            more = False
        elif yesno.upper() == "Y" or yesno.upper() == "YES":
            more = True
        else:
            print("Like, what? I just have no idea what you want from me, man")
            print("Thanks for stopping by, I guess")
            more = False 

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global tuition_type, full_tut, full_cap, full_inst, full_act, total, balance
    
    if inout == 1:
        tuition_type = "    IN-STATE"
        full_tut = RATE_TUITION_IN * numcredits
    elif inout == 2:
        tuition_type = "OUT-OF-STATE"
        full_tut = RATE_TUITION_OUT * numcredits
        full_cap = RATE_CAPITAL_FEE * numcredits
    else:
        print("\nInvalid; get out of here")

    full_inst = RATE_INSTITUTION_FEE * numcredits
    full_act = RATE_ACTIVITY_FEE * numcredits
    total = full_tut + full_inst + full_act
    balance = total - scholarshipamt

def display_results():
    print("\n-*-*-*-*-*- PVCC -*-*-*-*-*-")
    print("Tuition Type is ",tuition_type)
    print("Tuition Amount:    $",format(full_tut,"8,.2f"))
    if inout == 2:
        print("Capital Fee:       $",format(full_cap,"8,.2f"))
    print("Activity Fee:      $",format(full_act,"8,.2f"))
    print("Total:             $",format(total,"8,.2f"))
    print("Scholarship:       $",format(scholarshipamt,"8,.2f"))
    print("Balance:           $",format(balance,"8,.2f"))
    print(str(datetime.datetime.now()))

##call on main program to execute##
main()
