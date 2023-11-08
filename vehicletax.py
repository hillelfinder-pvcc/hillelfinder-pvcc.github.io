#Name: Hillel Finder
#Prog Purpose: this program computes vehicle fees

import datetime
#define rates
PERSONAL_PROP_TAX_RATE = 0.042
PERSONAL_PROP_TAX_RELIEF = 0.33

#define global variables
assessed_value = 0
relief_eligible = 0
annual_tax_amount = 0
half_annual_tax_amount = 0
relief_value = 0
relief_type = 0
total_due = 0

##define program functions
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to tax another vehicle? (Y/N): ")
        if yesno.upper() == "N" or yesno.upper() == "NO":
            print("Thanks for stopping by!")
            more = False
        elif yesno.upper() == "Y" or yesno.upper() == "YES":
            more = True
        else:
            print("How dare you?! Now you've insulted the Tax-Man!!")
            print("Thanks for stopping by, and we'll see you in court! :)")
            more = False 

def get_user_data():
    global assessed_value, relief_eligible

    assessed_value = int(input("What is the assessed value of your vehicle? "))
    relief_eligible = input("Are you eligible for tax relief (Y/N)? ")

def perform_calculations():
    global half_annual_tax_amount, annual_tax_amount, relief_value, relief_type, total_due

    annual_tax_amount = assessed_value * PERSONAL_PROP_TAX_RATE
    half_annual_tax_amount = annual_tax_amount / 2

    if relief_eligible.upper() == "Y" or relief_eligible.upper() == "YES":
        relief_value = half_annual_tax_amount * PERSONAL_PROP_TAX_RELIEF
        relief_type = "YES"
    else:
        relief_value = 0
        relief_type = " NO"

    total_due = half_annual_tax_amount - relief_value

def display_results():
    print("\n-*-*-*-*-*- Personal Property Tax, 2nd Half 2023 -*-*-*-*-*-")
    print("-*-*-*-*-*-*-*-*-*-*-*- 2nd Half 2023 *--*-*-*-*-*-*-*-*-*-*")
    print("Assessed Value of Vehicle:                        $",format(assessed_value,"8,.2f"))
    print("Full Annual Amount Owed:                          $",format(annual_tax_amount,"8,.2f"))
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Half-Annual Amount Owed:                          $",format(half_annual_tax_amount,"8,.2f"))
    print("Eligible for Relief?                                    ",relief_type)
    if relief_value != 0:
        print("Relief Amount:                                    $",format(relief_value,"8,.2f"))
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Total Due:                                        $",format(total_due,"8,.2f"))
    print(str(datetime.datetime.now()))

##call on main program to execute##
main()
