# Name: Hillel Finder
# Prog Purpose: This program creates a payroll report
import datetime
############## LISTS of data ############
emp = [
"Smith, James     ",
"Johnson, Patricia",
"Williams, John   ",
"Brown, Michael   ",
"Jones, Elizabeth ",
"Garcia, Brian    ",
"Miller, Deborah  ",
"Davis, Timothy   ",
"Rodriguez, Ronald",
"Martinez, Karen  ",
"Hernandez, Lisa  ",
"Lopez, Nancy     ",
"Gonzales, Betty  ",
"Wilson, Sandra   ",
"Anderson, Margie ",
"Thomas, Daniel   ",
"Taylor, Steven   ",
"Moore, Andrew    ",
"Jackson, Donna   ",
"Martin, Yolanda  ",
"Lee, Carolina    ",
"Perez, Kevin     ",
"Thompson, Brian  ",
"White, Deborah   ",]
job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
"C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]
hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
28, 31, 37, 32, 36, 22, 28, 29, 21, 31]
num_emps = len(emp)

##new lists for calculated amounts##
gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
ret = []
net_pay = []

total_gross = 0
total_net = 0

##tuples of constants##
PAY_RATE = (16.5, 15.75, 15.75, 19.5)

DED_RATE = (0.12, 0.03, 0.062, 0.0145, 0.04)

##define program functions##
def main():
    perform_calculations()
    create_output_file()

def perform_calculations():
    global total_gross, total_net

    for i in range(num_emps):
        #calculate gross pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]
        else:
            pay = hours[i] * PAY_RATE[3]

        #calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        soco = pay * DED_RATE[2]
        med = pay * DED_RATE[3]
        reti = pay * DED_RATE[4]

        net = pay - fed - state - soco - med - reti

        total_gross += pay
        total_net += net

        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(soco)
        medicare.append(med)
        ret.append(reti)
        net_pay.append(net)

def create_output_file():
    ###output files###
    out_file = "payroll.txt"
    f = open(out_file,"w")
    
    f.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n*************************************************************** FRESH FOOT MARKET ***************************************************************")
    f.write("\n------------------------------------------------------------- Weekly Payroll Report -------------------------------------------------------------")
    f.write("\n\t\t\t\t\t\t\t   "+str(datetime.datetime.now()))
    f.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------")
    
    f.write("\nEmp Name\t\tCode\tHours\t   Gross\tFed Inc Tax\tState Inc Tax\t    Soc Sec\t   Medicare\t  Retirement\t    Net")
    f.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------")

    for i in range(num_emps):
        f.write("\n"+str(emp[i])+"\t"+
              str(job[i])+"\t"+
              str(hours[i])+"\t"+
              format(gross_pay[i],'8,.2f')+"\t"+
              format(fed_tax[i],'8,.2f')+"\t"+
              format(state_tax[i],'8,.2f')+"\t"+
              format(soc_sec[i],'8,.2f')+"\t"+
              format(medicare[i],'8,.2f')+"\t"+
              format(ret[i],'8,.2f')+"\t"+
              format(net_pay[i],'8,.2f'))

    f.write("\n-------------------------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n************************************************************************************************************** TOTAL GROSS: $" + format(total_gross,'8,.2f'))
    f.write("\n************************************************************************************************************** TOTAL NET  : $ " + format(total_net,'8,.2f'))

    f.close()
    print("Open " + out_file + " to view your report")
##call on main program to execute##
main()
