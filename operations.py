
def client_name():
    while True:

        client_name = input("Enter your name:")
        if client_name.isalpha():
            break
        else:
            print("Error: Enter the valid name...!")

    return client_name      

def location():
    while True:

        location = input("Enter your location:")
        if location.isalpha():
            break
        else:
            print("Error: Enter the valid location...!")

    return location          

def contactnumber():
    while True:

        contactnumber = input("Enter your phone number ")
        if contactnumber.isdigit():
            break
        else:
            print("Error: Enter the valid contact number...!")
    
    return contactnumber

def ID_Number(Laptops):
    laptopNumber = None

    while not laptopNumber:

        laptopNumber = input("Please enter the ID of the laptop that you wanna buy")

        if not laptopNumber.isdigit():
            print("Error: Invalid ID...!")
            laptopNumber = None

        elif int(laptopNumber) <= 0 or int(laptopNumber) > len(Laptops):
            print("Error: The ID is not mentioned in the list above...!")
            laptopNumber = None
    
    return int(laptopNumber)

def selection(Laptops, idnumber):
    QuantitySelection = Laptops[idnumber][3]
    try:
        while True:
            count = input("How many does the customer want to buy? ")
            if count.isdigit():
                count = int(count)
                if count <= 0 or count > int(QuantitySelection):
                    print("Dear Admin, the selected quantity is not available in our shop. Please look again in the table.")
                    print("\n")
                    break
                else:
                    print("\n")
                    print("The product is available!")
                    break
            else:
                print("Error: Please enter a number")
    except(ValueError):
        print("Error: Please enter a number")

    return count

def update_file(Laptops, idnumber, Choosing ):
    # Update laptopDictionary with new quantity
    if Laptops[idnumber][3] != "0":

        Laptops[idnumber][3] = str(int(Laptops[idnumber][3]) - int(Choosing))

    # Create a list to store the updated laptops
    laptopList = []
    for values in Laptops.values():
        laptopList.append(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]))

    # Write the updated laptops to the file
    with open("laptopsdetails.txt", "w") as file:
        file.write(''.join(laptopList))

    return laptopList

def forbill(buylaptop, Laptops, idnumber, Choosing):
    product_name = Laptops[idnumber][0]
    manufacturer_name = Laptops[idnumber][1]
    userquantity = Choosing
    laptop_price = Laptops[idnumber][2].replace("$","")
    total_price = int(laptop_price) * int(userquantity)


    buylaptop.append([product_name, manufacturer_name, userquantity, laptop_price, total_price])

    return buylaptop



def quantity_check(Laptops, idnumber): 

    while True: # Using while loop

        quantity = input("Enter the quantity: ") # Asking user for input
        if quantity.isdigit():
            quantity = int(quantity)
            laptop_selected = Laptops[idnumber][3] # Quantity is accessed using [laptop_id] = key and [3] = index

            if quantity > 0: # If the quantity is greater than zero it returns quantity
                return quantity
            else: # Shows an error message
                print("Quantity error. Please enter a valid quantity.") 
        else:
            print("Error: Please enter a number")

# Defining items restock function
def Items_restock(Laptops, idnumber, qty): 
    Laptops[idnumber][3] = int(Laptops[idnumber][3]) + int(qty) # increase the quantity of the selected laptop

    laptop_data = [",".join(map(str, info)) for info in Laptops.values()]
    data_to_write = "".join(laptop_data)

    with open("laptops.txt", "w") as file:
        file.write(data_to_write)

# Defining the data restock function
def data_restocks(restock_purchased_laptop, Laptops, idnumber, qty):
    productname = Laptops[idnumber][0]
    companyname = Laptops[idnumber][1]
    selected_qty = qty
    laptopPrice = Laptops[idnumber][2].replace("$", "")
    selectedItemPrice = Laptops[idnumber][2].replace("$", "")
    totalPrice = int(selectedItemPrice) * int(selected_qty)
   

    restock_purchased_laptop.append([productname, companyname, selected_qty, laptopPrice, totalPrice])
    return restock_purchased_laptop