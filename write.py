from operations import *
from read import *

def buying(userInfo,  total, NameOfClient, datestring,  ContactOfCustomer, locationOfCustomer):
    shippingCost = 1500
    print("\n")
    print("\t\t\t\t---------------------------")
    print("\t\t\t\t   Dahal Laptop Shop")
    print("\t\t\t\t---------------------------")
    print("\t\t\t\t         Your bill ")
    print("Date: " + str(datestring))
    print("Customer Name: " + str(NameOfClient)) 
    print("Customer Phone Number: " + str(ContactOfCustomer))
    print("Customer location: " + str( locationOfCustomer))
    print("------------------------------------------------------------------------------------------")
    print("\t\t\t\t      Laptop Details: ")
    print("------------------------------------------------------------------------------------------")
    print("Item name \t Company Name \t\t  Total Quantity \t Laptop Price \t    Total")
    print("------------------------------------------------------------------------------------------")
    print("\n")
    for i in userInfo:
        print(i[0], "    ", i[1], "\t\t      ", i[2], "\t\t  ", "$" , i[3], "\t  " , "$" , i[4])
    print("\n")
    print("------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGrand Total: " + "$" + str(total))
    print("Your Shopping Cost is: $", shippingCost)
    sp = total + 1500
    print("Grand Total(With Shipping cost)", "$ ", sp)
    print("\n")
    print("\t\t    ------------------------------------------------")
    print("\t\t      THANK YOU FOR Dahal Laptop Shop!")
    print("\t\t    ------------------------------------------------")
    print("\n")

    return sp

def txt_bill(userInfo, total, NameOfClient, datestring,  ContactOfCustomer, locationOfCustomer):
    sp = total + 500
    shippingCost = 1500
    file = open(str(NameOfClient) + str(datestring) + ".txt", "w")
    file.write("\t\t\t\t\t\t\t\t---------------------------")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t   Dahal Laptop Shop")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t---------------------------")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t        Your bill ")
    file.write("\n")
    file.write("Date: " + str(datestring))
    file.write("\n")
    file.write("Customer Name: " + str(NameOfClient))
    file.write("\n")
    file.write("Customer Phone Number: " + str(ContactOfCustomer))
    file.write("\n")
    file.write("Customer location: " + str( locationOfCustomer))
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t      Laptop Details: ")
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write(
        "Item name \t\t\t Company Name \t\t\t Total Quantity \t\t Laptop Price \t\t Total")
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------")
    file.write("\n\n")
    for i in userInfo:
        file.write(str(i[0]) + "\t\t" + str(i[1]) + "\t\t\t\t\t   " + str(i[2]) + "\t\t\t\t" + "$" + str(i[3]) + "\t\t" + "$" + str(i[4]) + "\n")
    file.write("\n")
    file.write("----------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Grand Total: " + "$" + str(total))
    file.write("\n")
    file.write("Your Shipping Cost is: $" + str(shippingCost))
    file.write("\n")
    for i in userInfo:
        file.write("Grand Total(With Shipping cost): $" + str(sp))
    file.write("\n\n")
    file.write("\t\t\t\t\t\t    ------------------------------------------------")
    file.write("\n")
    file.write("\t\t\t\t\t\t      THANK YOU FOR CHOOSING Dahal Laptop Shop!")
    file.write("\n")
    file.write("\t\t\t\t\t\t    ------------------------------------------------")
    file.write("\n")

def bill_restock(Laptops, idnumber, restock, total, vat, NameOfClient, datestring):
    laptopPrice = Laptops[idnumber][2].replace("$", "")
    print("\n")
    print("\t\t\t\t---------------------------")
    print("\t\t\t\t   Dahal Laptop Shop")
    print("\t\t\t\t---------------------------")
    print("\t\t\t\t         Your bill ")
    print("Date:" + str(datestring))
    print("Customer Name: " + str(NameOfClient))
    print("-------------------------------------------------------------------------------")
    print("\t\t\t\t      Laptop Details: ")
    print("-------------------------------------------------------------------------------")
    print("Item name \t Company Name \t\t  Total Quantity \t Laptop Price")
    print("-------------------------------------------------------------------------------")
    print("\n")
    for i in restock:
        print(i[0], "    ", i[1], "\t\t      ", i[2], "\t\t  ", "$" , i[3])
    print("\n")
    print("-------------------------------------------------------------------------------")
    print(f"The Grand Total is: $ {int(total) * int(laptopPrice)}") 

    print("Price with 13% Vat: $", vat)
    print("\n")
    print("\t\t    ------------------------------------------------")
    print("\t\t      THANK YOU FOR CHOOSING Dahal Laptop Shop!")
    print("\t\t    ------------------------------------------------")
    print("\n")

def bill_restock_store(Laptops, idNumber, restock, total, vat, NameOfClient, datestring):
    laptopPrice = Laptops[idNumber][2].replace("$", "")
    file = open(f"Restock_{NameOfClient}{datestring}.txt","w")
    file.write("\n")
    file.write("\t\t\t\t---------------------------")
    file.write("\n")
    file.write("\t\t\t\t   Dahal Laptop Shop")
    file.write("\n")
    file.write("\t\t\t\t---------------------------")
    file.write("\n")
    file.write("\t\t\t\t         Your bill ")
    file.write("\n")
    file.write("Date:" + str(datestring))
    file.write("\n")
    file.write("Customer Name: " + str(NameOfClient))
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t\t\t\t      Laptop Details: ")
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Item name \t\t Company Name \t\t  Total Quantity \t\t Laptop Price")
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\n")
    for i in restock:
        file.write(str(i[0])+ "         "+ str(i[1])+ "\t\t\t  "+ str(i[2])+ "\t\t         "+ "$" +str(i[3]) + "\n")
    file.write("\n")
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write(f"The Grand Total is: ${int(total) * int(laptopPrice)}") 
    file.write("\n")
    file.write("Price with 13% Vat: $"+ str(vat))    
    file.write("\n")
    file.write("\n")
    file.write("\t\t    ------------------------------------------------")
    file.write("\n")
    file.write("\t\t      THANK YOU FOR CHOOSING Dahal Laptop Shop!")
    file.write("\n")
    file.write("\t\t    ------------------------------------------------")
    file.write("\n")