#Name: Hillel Finder
#Program Purpose: This program uses lists to find the personal property tax for vehicles in Charlottlesville
#   and produces a report which displays all data and the total tax due

#Personal property tax in Charlottesville:
#       -- $4.20 per $100 of vehicle value (4.20% per year)
#       __ Paid every 6 months
#Personal Property Tax Relief (PPTR):
#       -- Eligibility: Owned or leased vehicles which are predominantly used for non-busisness purposes & have passenger license plates
#       -- Tax relief for qualified vehicle is 33%

import datetime

##define tax rates##
PPT_RATE = 0.042
RELIEF_RATE = 0.33

##create list data##
vehicle = ["2019 Volvo ",
           "2018 Toyota",
           "2022 Kia   ",
           "2020 Ford  ",
           "2023 Honda ",
           "2019 Lexus ",]

vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700]

pptr_eligible = ["Y","Y","N","Y","N","Y",]

owner_name = ["Brand, Debra      ",
              "Smith, Carter     ",
              "Johnson, Bradley  ",
              "Garcia, Jennifer  ",
              "Henderson, Leticia",
              "White, Danielle   ",]

ppt_owed = []

num_vehicles = len(vehicle)
tax_due = 0
total = 0


##define program functions##

def main():
    date()
    perform_calculations()
    display_results()

def date():
    global monthname, day, year
    today = str(datetime.datetime.now())

    month = today[5:7]
    day = today[8:10]
    year = today[0:4]

    monthname = ""
    if month == "01":
        monthname = "January"
    elif month == "02":
        monthname = "Febuary"
    elif month == "03":
        monthname = "March"
    elif month == "04":
        monthname = "April"
    elif month == "05":
        monthname = "May"
    elif month == "06":
        monthname = "June"
    elif month == "07":
        monthname = "July"
    elif month == "08":
        monthname = "August"
    elif month == "09":
        monthname = "September"
    elif month == "10":
        monthname = "October"
    elif month == "11":
        monthname = "November"
    else:
        monthname = "December"

def perform_calculations():
    global total

    for i in range(num_vehicles):

        tax_due = (vehicle_value[i] * PPT_RATE) / 2

        if pptr_eligible == "Y":
            tax_due = tax_due * 0.67

        ppt_owed.append(tax_due)

        total = total + tax_due

def display_results():
    moneyf = '8,.2f'
    line = ("------------------------------------------------------------------------")
    tab = "\t"

    print(line)
    print("********************* PERSONAL PROPERTY TAX REPORT *********************")
    print("                        Charlottesville, Virginia")

    print("\n\t\t" + monthname + " " + day + ", " + year + tab + str(datetime.datetime.now()))
    print("\nNAME" + tab + tab + tab + "VEHICLE" + tab + tab + "VALUE" + tab + tab + "RELIEF" + tab +" TAX DUE")
    print(line)

    for i in range(num_vehicles):
        dataline1 = owner_name[i] + tab + vehicle[i] + tab + format(vehicle_value[i],moneyf) + tab
        dataline2 = pptr_eligible[i] + tab + format(ppt_owed[i],moneyf)
        print(dataline1 + dataline2)

    print(line)
    print("**************************************** TOTAL TAX DUE: " + tab + format(total,moneyf))

main()
