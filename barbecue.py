#Name: Hillel Finder
#Name: Keano Mckeithan
#Program Purpose: This program finds the cost of barbecue stuff
#   Price for adult: $19.95
#   Price for children: $11.95
#   Service fee: 10%
#   Sale tax rate: 6.2%

import datetime

## define global variables ##
#define tax rate and prices
SALES_TAX_RATE = 0.062
SERVICE_FEE = 0.10

PR_ADULT = 19.95
PR_CHILD = 11.95

#define global variables
num_adult = num_child = 0
subtotal = 0
serv_fee = 0
sales_tax = 0
total = 0

##define program functions ##
def main():

    more_tickets = True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_result()

        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper() == "N":
            more_tickets = False
            print("Thank you for your order. Enjoy your BBQ!")

def get_user_data():
    global num_adult, num_child
    num_adult = int(input("Number of adults: "))
    num_child = int(input("Number of children: "))

def perform_calculations():
    global subtotal, serv_fee, sales_tax, total
    subtotal = (num_adult * PR_ADULT) + (num_child * PR_CHILD)
    serv_fee = subtotal * SERVICE_FEE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax + serv_fee
    
def display_result():
    print('----------------------------------')
    print('**** BRANCH BARBECUE BUFFET   ****')
    print('**** Your neighborhood BBQ :) ****')
    print('----------------------------------')
    print('Adults                  $ ' + format(num_adult * PR_ADULT, '8,.2f'))
    print('Children                $ ' + format(num_child * PR_CHILD, '8,.2f'))
    print('Subtotal                $ ' + format(subtotal, '8,.2f'))
    print('Service Fee             $ ' + format(serv_fee, '8,.2f'))
    print('Sales Tax               $ ' + format(sales_tax, '8,.2f'))
    print('Total                   $ ' + format(total, '8,.2f'))
    print('----------------------------------')
    print(str(datetime.datetime.now()))

## call on main program to execute ##
main()
