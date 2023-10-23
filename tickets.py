#Name: Hillel Finder
#Program Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Sale tax rate: 5.5%

import datetime

## define global variables ##
#define tax rate and prices
SALES_TAX_RATE = 0.055
PR_TICKET = 10.99
PR_POPCORN = 12.99
PR_DRINK = 4.99

#define global variables
num_tickets = num_popcorn = num_drink = 0
subtotal = 0
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
            print("Thank you for order. Enjoy your movie!")

def get_user_data():
    global num_tickets, num_popcorn, num_drink
    num_tickets = int(input("Number of movie tickets: "))
    num_popcorn = int(input("Number of popcorn buckets: "))
    num_drink = int(input("Number of drinks: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = (num_tickets * PR_TICKET) + (num_popcorn * PR_POPCORN) + (num_drink * PR_DRINK)
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    
def display_result():
    print('-----------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('-----------------------------')
    print('Tickets            $ ' + format(num_tickets * PR_TICKET, '8,.2f'))
    print('Popcorn            $ ' + format(num_popcorn * PR_POPCORN, '8,.2f'))
    print('Drinks             $ ' + format(num_drink * PR_DRINK, '8,.2f'))
    print('Sales Tax          $ ' + format(sales_tax, '8,.2f'))
    print('Total              $ ' + format(total, '8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

## call on main program to execute ##
main()
