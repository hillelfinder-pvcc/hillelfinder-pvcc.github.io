#Name: Hillel Finder
#Program Purpose: This program is my final project for this class
#It takes data from a file, then creates a webpage showing a hotel registry

import datetime

##############  define global variables ############
# define tax rate and prices
SINGLE_PRICE = 195
DOUBLE_PRICE = 250
SUITE_PRICE = 350

SALES_TAX_RATE = 0.065
OCC_TAX_RATE = 0.1125

subtotal = 0
sales_tax = 0
occ_tax = 0
total = 0
grand_total = 0

# create output file
outfile = 'hotelsalesrep.html'

##############  define program functions ################
def main():
    read_in_cust_file()
    open_outfile()    
    perform_calculations()
    display_results()

    print('\n** Open this file in a browser window to see your results: ' + outfile)
    f.write('</body></html>')
    f.close()

def read_in_cust_file():
    global cust
    cust_data = open("emerald.csv","r")
    cust_in = cust_data.readlines()
    cust_data.close()

    #split the data into fields
    cust = []
    for i in cust_in:
        cust.append(i.split(","))

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Hotel Beach Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #64a691; background-image: url(Leonardo_Diffusion_XL_Emerald_Beach_Hotel_and_Resort_2.jpg); background-size: cover; color: #f8dd61;">\n')

def perform_calculations():
    global subtotal, sales_tax, occ_tax, total, grand_total

    for i in range(len(cust)):
        if cust[i][2] == "SR":
            night_rate = SINGLE_PRICE
        elif cust[i][2] == "DR":
            night_rate = DOUBLE_PRICE
        else:
            night_rate = SUITE_PRICE

        subtotal = night_rate * int(cust[i][3])
        sales_tax = subtotal * SALES_TAX_RATE
        occ_tax = subtotal * OCC_TAX_RATE
        total = subtotal + sales_tax + occ_tax

        cust[i].append(subtotal)
        cust[i].append(sales_tax)
        cust[i].append(occ_tax)
        cust[i].append(total)

        grand_total += total

def display_results():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    sp = " "

    trcj = '<tr><td style=text-align:center>'
    endtdcj = '</td><td style=text-align:center>'
    trlj = '<tr><td style=text-align:left>'
    endtdlj = '</td><td style=text-align:left>'

    f.write('<table border="3" style ="background-color: #602227e0;  font-family: arial, Verdana, Geneva; margin: auto;">') #47161a
    f.write('<tr><td colspan = 8 style=text-align:center>')
    f.write('<h2>EMERALD BEACH HOTEL & RESORT</h2></td></tr>')
    f.write('<tr><td colspan= "8" style=text-align:center>Sales Report Date/Time: ')
    f.write(day_time)
    
    f.write(trcj + 'Last' + endtdcj + 'First' + endtdcj + 'Room Type' + endtdcj + 'Num. Nights' + endtdcj +
            'Subtotal' + endtdcj + 'Sales Tax' + endtdcj + 'Occ. Tax' + endtdcj + 'Total' + endtr)
    for i in range(len(cust)):
        f.write(trlj + str(cust[i][0]) + endtdlj + str(cust[i][1]) + endtdcj + str(cust[i][2]) + endtdcj + str(cust[i][3]) + endtd
                + str(format(cust[i][4],currency)) + endtd + str(format(cust[i][5],currency)) + endtd
                + str(format(cust[i][6],currency)) + endtd + str(format(cust[i][7],currency)) + endtr)
    f.write('<tr><td colspan= "8">Grand Total: ' + str(format(grand_total,currency)))
    f.write(endtr)
    f.write('</table>')

##########  call on main program to execute ############
main()              
