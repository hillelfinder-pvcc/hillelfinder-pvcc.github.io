#Name: Hillel Finder
#The purpose of this program finds the cost of pet vaccines & medications for dogs and cats

import datetime

##define global variables##
#define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEP = 21
PR_LYDI = 41
PR_RAB = 25

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

#define cat prices
PR_FELU = 35
PR_FEVIRH = 30
PR_CATRAB = 25

PR_CATCHEWS = 8

##define program functions##
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D" or pet_type.upper() == "DOG":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()


        elif pet_type.upper() == "C" or pet_type.upper() == "CAT":
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()  

        else:
            print("\nInvalid Pet-Type.")

        askAgain = input("\nWould you like to process another pet (Y/N)?: ")
        if askAgain.upper() == "N":
            more = False
            print("Thank you for trusting PET CARE MEDS with your pet vaccines and medications.")

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")
    pet_type = input("Is this pet a dog (D) or cat (C)? ")
    pet_weight = int(input("Weight of your pet (in pounds): "))

##Dog Functions##

def get_dog_data():
    global pet_vax_type, num_chews, pet_type
    pet_type = "DOG"
    dog1 = "\n** Dog Vaccines: \n\t1.Bordatella     ($30.00)\n\t2.DAPP           ($35.00)\n\t3.Influenza      ($48.00)\n\t4.Leptosprirosis ($21.00)"
    dog2 = "\n\t5.Lyme Disease   ($41.00)\n\t6.Rabies         ($25.00)\n\t7.Full Package   ($170.00; 15% OFF!)\n\t8.NONE"
    dogmenu = dog1 + dog2
    pet_vax_type = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevenion medication is recommended for all dogs.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name.upper() + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heartworm chews would you like to order? "))
    else:
        num_chews = 0

def perform_dog_calculations():
    global vax_cost, chews_cost, total, vax_name, chew_name

    ##vaccines
    if pet_vax_type == 1:
        vax_cost = PR_BORD
        vax_name = "Bordatella                  "

    elif pet_vax_type == 2:
        vax_cost = PR_DAPP
        vax_name = "DAPP                        "

    elif pet_vax_type == 3:
        vax_cost = PR_FLU
        vax_name = "Influenza                   "

    elif pet_vax_type == 4:
        vax_cost = PR_LEP
        vax_name = "Leptosprirosis              "

    elif pet_vax_type == 5:
        vax_cost = PR_LYDI
        vax_name = "Lyme Disease                "

    elif pet_vax_type == 6:
        vax_cost = PR_RAB
        vax_name = "Rabies                      "

    elif pet_vax_type == 7:
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU + PR_LEP + PR_LYDI + PR_RAB
        vax_cost = 0.85 * PR_ALL
        vax_name = "Full Package                "

    else:
        vax_cost = 0
        vax_name = "NONE                        "

    ##heart worm chews
    if num_chews != 0:
        if pet_weight < 25:
            chews_cost = num_chews * PR_CHEWS_SMALL
            chew_name = "Small-Dog Chews "

        elif pet_weight >= 26 and pet_weight < 50:
            chews_cost = num_chews * PR_CHEWS_MED
            chew_name = "Medium-Dog Chews"

        else:
            chews_cost = num_chews * PR_CHEWS_LARGE
            chew_name = "Large-Dog Chews "
    else:
        chews_cost = 0
    ##find total
    total = vax_cost + chews_cost

def display_dog_results():
    print('-----------------------------------------------------------------------')
    print('**************************** PET CARE MEDS ****************************')
    print('                     Your neighborhood animal house                    ')
    print('-----------------------------------------------------------------------')
    print('Animal Name:', pet_name.upper(), '\tPet Type is', pet_type, '\t Pet Weight is', pet_weight, 'pounds')
    print('Vaccine Type is:', vax_name, '                $' + format(vax_cost, '8,.2f'))
    if num_chews != 0:
        print('Chew Type is', chew_name, '                                $' + format(chews_cost, '8,.2f'))
    print('Total                                                         $' + format(total, '8,.2f'))
    print('-----------------------------------------------------------------------')
    print(str(datetime.datetime.now()))

##CAT functions##
def get_cat_data():
    global pet_vax_type, num_chews, pet_type
    pet_type = "CAT"
    cat1 = "\n** Cat Vaccines: \n\t1.Feline Leukemia              ($35.00)\n\t2.Feline Viral Rhinotracheitis ($30.00)"
    cat2 = "\n\t3.Rabis (one year)             ($25.00)\n\t4.Full Package                 ($81.00; 10% OFF!)\n\t5.NONE"
    catmenu = cat1 + cat2
    pet_vax_type = int(input(catmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevenion medication is recommended for all cats.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name.upper() + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heartworm chews would you like to order? "))
    else:
        num_chews = 0

def perform_cat_calculations():
    global vax_cost, chews_cost, total, vax_name

    ##vaccines
    if pet_vax_type == 1:
        vax_cost = PR_FELU
        vax_name = "Feline Leukemia             "

    elif pet_vax_type == 2:
        vax_cost = PR_FEVIRH
        vax_name = "Feline Viral Rhinotracheitis"

    elif pet_vax_type == 3:
        vax_cost = PR_CATRAB
        vax_name = "Rabies (one year)           "

    elif pet_vax_type == 4:
        PR_ALL = PR_FELU + PR_FEVIRH + PR_CATRAB
        vax_cost = 0.90 * PR_ALL
        vax_name = "Full Package                " 

    else:
        vax_cost = 0
        vax_name = "NONE                        "

    ##heart worm chews
    if num_chews != 0:
        chews_cost = num_chews * PR_CATCHEWS
    else:
        chews_cost = 0
    ##find total
    total = vax_cost + chews_cost

def display_cat_results():
    print('-----------------------------------------------------------------------')
    print('**************************** PET CARE MEDS ****************************')
    print('                     Your neighborhood animal house                    ')
    print('-----------------------------------------------------------------------')
    print('Animal Name:', pet_name.upper(), '\tPet Type is', pet_type, '\t Pet Weight is', pet_weight, 'pounds')
    print('Vaccine Type is:', vax_name, '                $' + format(vax_cost, '8,.2f'))
    if num_chews != 0:
        print('Feline Chews                                                  $' + format(chews_cost, '8,.2f'))
    print('Total                                                         $' + format(total, '8,.2f'))
    print('-----------------------------------------------------------------------')
    print(str(datetime.datetime.now()))

main()
