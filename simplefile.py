#Name: Hillel Finder
#Program Purpose: This program uses a data file

def main():
    read_in_cust_file()
    display_cust_list()

def read_in_cust_file():
    global cust
    cust_data = open("customer_data_file.txt","r")
    cust_in = cust_data.readlines()
    cust_data.close()

    #split the data into fields
    cust = []
    for i in cust_in:
        cust.append(i.split(","))

def display_cust_list():
    total = 0

    print("-----------------------------------")
    print("****** CUSTOMER SALES REPORT ******\n")
    for i in range(len(cust)):
        amt_owed = float(cust[i][2]) * 1.1
        total += amt_owed
        print(cust[i][1] + "     \t" + cust[i][0]+ "\t" + format(amt_owed,"8,.2f"))

    print("------_----------------------------")
    print("**** TOTAL AMOUNT:   \t" + format(total,"8,.2f"))

main()
