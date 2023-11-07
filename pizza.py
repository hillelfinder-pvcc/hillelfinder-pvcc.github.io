#Name: Hillel Finder
#Name: Finn Zschaebitz
#Prog Purpose: this program computes pizza fees

import datetime
#define food and drink rates
SMALL_PIZZA_FEE = 9.99
MEDIUM_PIZZA_FEE = 12.99
LARGE_PIZZA_FEE = 17.99
EXTRA_LARGE_PIZZA_FEE = 21.99

DRINK_FEE = 3.99
BREADSTICKS = 6.99
SALES_TAX_RATE = 0.055

#define global variables
pizza_type = 0
num_pizza = 0
num_drink = 0
num_bread = 0

full_pizza = 0
full_drink = 0
full_bread = 0
subtotal = 0
sales_tax = 0
total = 0

##define program functions
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        if pizza_type != 0:
            display_results()
        yesno = input("\nWould you like to place another order? (Y/N): ")
        if yesno.upper() == "N" or yesno.upper() == "NO":
            print("Thanks for stopping by!")
            more = False
        elif yesno.upper() == "Y" or yesno.upper() == "YES":
            more = True
        else:
            print("Like, what? Now you've insulted the Pizza-Man!!")
            print("Thanks for stopping by, I guess")
            more = False 

def get_user_data():
    global pizza_type, num_pizza, num_drink, num_bread

    menu = "\n** Pizza Sizes: \n\t1.Small \n\t2.Medium \n\t3.Large \n\t4.Extra-Large"
    pizza_type = int(input(menu + "\nWhat size of Pizza do you want? "))
    num_pizza = int(input("How many Pizzas? "))
    num_drink = int(input("How many Drinks? "))
    num_bread = int(input("How many Breadsticks? "))

def perform_calculations():
    global pizza_type, full_pizza, full_drink, full_bread, sales_tax, subtotal, total

    if pizza_type == 1:
        pizza_type = "               Small Pizza"
        full_pizza = SMALL_PIZZA_FEE * num_pizza
    elif pizza_type == 2:
        pizza_type = "              Medium Pizza"
        full_pizza = MEDIUM_PIZZA_FEE * num_pizza
    elif pizza_type == 3:
        pizza_type = "               Large Pizza"
        full_pizza = LARGE_PIZZA_FEE * num_pizza
    elif pizza_type == 4:
        pizza_type = "         Extra-Large Pizza"
        full_pizza = EXTRA_LARGE_PIZZA_FEE * num_pizza
    else:
        print("\nInvalid; get out of here")
        pizza_type = 0

    full_drink = DRINK_FEE * num_drink
    full_bread = BREADSTICKS * num_bread
    subtotal = full_pizza + full_drink + full_bread
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print("\n-*-*-*-*-*- BIG HONK'N PIZZAS -*-*-*-*-*-")
    print("Pizza Type is ",pizza_type)
    print("Number of Pizzas Ordered:       ",format(num_pizza,"8,"))
    print("Pizza Fee:                     $",format(full_pizza,"8,.2f"))
    print("Drink Fee:                     $",format(full_drink,"8,.2f"))
    print("Breadstick Fee:                $",format(full_bread,"8,.2f"))
    print("Sales Tax:                     $",format(sales_tax,"8,.2f"))
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("Total:                         $",format(total,"8,.2f"))
    print(str(datetime.datetime.now()))

##call on main program to execute##
main()
