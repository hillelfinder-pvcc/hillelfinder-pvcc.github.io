#Name: Hillel Finder
#Prog Purpose: the program comuters PVCC college tuition & fees based on number of credits, output as an HTML file
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

# create output file
outfile = 'tuition.html'

##define program functions
def main():

    open_outfile()
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        if inout == 1 or inout == 2:
            output_results()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.upper() == "N" or yesno.upper() == "NO":
            print("Thanks for stopping by!")
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()
        elif yesno.upper() == "Y" or yesno.upper() == "YES":
            more = True
        else:
            print("Like, what? I just have no idea what you want from me, man")
            print("Thanks for stopping by, I guess")
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuition </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #ffffff; background-image: url(Piedmont_VA_Comm_College_logo.jpeg); background-size: 250px 250px; color: #d5414f;">\n')
    
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

def output_results():
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    trlj = '<tr><td style=text-align:left>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    sp = " "

    #style="background-color: #418cd0;"

    f.write('\n<table border="3" style ="background-color: #ffffff;  font-family: arial, Tahoma, Verdana,; margin: auto;">\n')            

    f.write('<tr style="background-color: #418cd0;"><td colspan = 3><h3></h3></tr>')
    f.write('<tr><td colspan = 3>\n')
    f.write('<h2>-*-*-*-*-*- PVCC -*-*-*-*-*-</h2></td></tr>')

    f.write(trlj + 'Tuition Type is: ' + endtd + tuition_type + endtr)
    f.write(trlj + 'Tuition Amount' + endtd + format(full_tut,"8,.2f") + endtr)
    if inout == 2:
        f.write(trlj + 'Capital Fee' + endtd + format(full_cap,"8,.2f") + endtr)
    f.write(trlj + 'Activity Fee' + endtd + format(full_act,"8,.2f") + endtr)
    f.write(trlj + 'Total' + endtd + format(total,"8,.2f") + endtr)
    f.write(trlj + 'Scholarship:' + endtd + format(scholarshipamt,"8,.2f") + endtr)
    f.write(trlj + 'Balance:' + endtd + format(balance,"8,.2f") + endtr)

    f.write('<tr><td colspan= "3" style=text-align:center>Date/Time: ')
    f.write(day_time)
    f.write(endtr)
    f.write('</table><br />')

##call on main program to execute##
main()
