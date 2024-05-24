import datetime 
from operations import *
from read import *
from write import *



Laptops = laptop()
file = open("laptopsdetails.txt","r")
mylaptop={}
now = datetime.datetime.now()
datestring = now.strftime("%Y-%m-%d%H-%M-%S")
total = 0



print(mylaptop)
print("\n")
print("_______________________________________________________________________________________________________________________________________")
print("\t\t\t\t\t\t\t Welcome to Dahal Laptop Shop")
print("_______________________________________________________________________________________________________________________________________")
print("\t\t\t\t\t\t\t location : New Baneshwor, Kathmandu")
print("_______________________________________________________________________________________________________________________________________")

continueloop = True
while continueloop == True:
    print("Press 1 to purchase the laptops from the manufacturers")
    print("Press 2 to sell the laptops to the customers")
    print("Press 3 to exit")
    print("\n")
    print("_______________________________________________________________________________________________________________________________________")

    input_userloop = True
    while input_userloop == True:
        input_user = input("Choose the above options")
        if input_user.isdigit():
            input_user = int(input_user)
            break
        else:
            print("\n")
            print("Error: Please choose the options above..!")

    buylaptop = []   
    restock_purchased_laptop = [] 
    if input_user == 1:

        NameOfClient = client_name()

        locationOfCustomer = location()

        ContactOfCustomer = contactnumber()

        BuyAgain = True
        while BuyAgain == True:

            OneMore = view_laptop()
            idnumber = ID_Number(Laptops)
            Choosing = selection(Laptops, idnumber)
            Update = update_file(Laptops, idnumber, Choosing )

            #User info

            userInfo = forbill(buylaptop, Laptops, idnumber, Choosing)

            #Another One

            AnotherOne = input("Do you want to buy another laptop? \nPress y to continue \nPress any other key to print the bill \n\nWhat do you want to do?").upper()
            print()
            if AnotherOne == "Y":
                BuyAgain = True
            else:
                BuyAgain = False
                for i in userInfo:
                    total += int(i[4])
                buying(userInfo,  total, NameOfClient, datestring,  ContactOfCustomer, locationOfCustomer)
                txt_bill(userInfo, total, NameOfClient, datestring,  ContactOfCustomer, locationOfCustomer)
                
                    
            

    elif input_user == 2:
        restockloop = True
        print("\n")
        NameOfClient = client_name()
        while restockloop == True:
            view_laptop()
            print("\n")
            Laptops = laptop()
            idnumber = ID_Number(Laptops)
            qty = quantity_check(Laptops, idnumber)
            qtn_restock = Items_restock(Laptops, idnumber, qty)
            anotheroneforrestock = input("Do you want to buy another laptop? \nPress y to continue \nPress any other key to print the bill \n\nWhat do you want to do?").upper()
            restock = data_restocks(restock_purchased_laptop, Laptops, idnumber, qty)

            if anotheroneforrestock == "Y":
                restockloop = True 
            else:
                restockloop = False
                laptopPrice = 0 
                for i in restock:
                    laptopPrice = int(i[3])
                    total += int(i[2])
                vat_price = laptopPrice * total
                vat = vat_price + (vat_price*0.13)
                bill_restock(Laptops, idnumber, restock, total, vat, NameOfClient, datestring)

        print("you pressed 2")  
    elif input_user == 3:
        print("Thanks for visiting Dahal Laptop Shop")   
        continueloop = False  
    else:
        print("Choose the options given")


