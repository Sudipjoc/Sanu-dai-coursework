def laptop():
    laptopSupplies = {}
    with open("laptopsdetails.txt", "r") as file:
        laptopId = 1
        lines = file.readlines()
        for line in lines:
            laptopSupplies[laptopId] = line.split(",")
            laptopId += 1

    return laptopSupplies


def view_laptop():
    print("Our Stocks:")
    print("-" * 88)
    print("S.N.\tLaptop Name\tCompany Name\tPrice\t     Quantity   Processor\tGraphics" )
    print("-" * 88)
    file = open("laptopsdetails.txt", "r")
    a = 1
    for line in file:
        print(a, "\t" + line.replace("," ,"\t").strip())
        a = a + 1
        print("-" * 88)
    file.close()