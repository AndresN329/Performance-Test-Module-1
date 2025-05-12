#el diccionary
Inventory = {"bread":(500, 12),
             "water":(1000, 20),
             "rice":(2500, 5),
             "eggs":(700, 30),
             "olive oil":(5500,6),
             } 

#Add product function
def add_products():
    try:
        NameP = input("Please enter the poduct name: ").lower().strip()

        if NameP in Inventory:    #check if it is already available
            print("The product is already available in inventory :)")
        else: 
            price = float(input("Please enter the price product: "))
            if price > 0:    #check that the price is greater than 0
                amount = int(input("Please enter the amount product: "))
                if amount > 0:     #heck that the amount is greater than 0
                    Inventory[NameP] = (price, amount) #stored in the inventary
                else:
                    print("The amount must be greater than 0")
            else:
                print("The price must be greater than 0")

            print("The product has been successfully registered :)")
    except ValueError:     #error control to avoid program failure
        print("PLease just enter valid values -_- ")

#Consult products fun
def consult_products():

    NameP = input("Please enter the product name to search: ").lower().strip()

    if NameP in Inventory:      #check if it is already available in inventory
        print("This prodct is available in inventory :0")    #message if it's available
        price, amount = Inventory[NameP]
        print(f"The product name is: {NameP}")
        print(f"The price is: {price}")
        print(f"The amount is: {amount}")
    else:
        print("This product is not available in inventory :(")  #message if the product is no in the inventory

#Udate prices function
def update_prices():
    try:
        NameP = input("Please enter the product name to update price: ").lower().strip()

        if NameP in Inventory:    #check if it is already available in inventory
            New_price = float(input("Please enter the new price: "))
            if New_price > 0:   #check if the new price is grater than 0
                amount = Inventory[NameP][1]
                Inventory[NameP] = (New_price,amount)
                print("The new price has been registred succesfuly")
            else:
                print("The new price must be greater than 0")   #if the price is less than 0 display this message
        else:
             print("This product in not available :(")

    except ValueError:
        print("PLease just enter valid values -_- ")    #error control to avoid program failure

#Delete produt function
def delete_produts():
    NameP = input("PLease enter the name product taht you want to delete: ").lower().strip()

    if NameP in Inventory:     #check if it is already available in inventory
        print(f"The product {NameP} is available in inventory")   #display that the product it's available
        del Inventory[NameP]    
        print(f"The product {NameP} has been delete from inventory")   #confirm the deletion
    else:
        print(f"{NameP} is not available in the inventory :(")    #if it is not available display this message

#calculate total inventory value
def total_inventory_value():
    total = 0
    for product in Inventory: #for loop to see all products
        price, amount = Inventory[product]
        total += price * amount #Multiply price by quantity and the result is stored in the variable "total"
        print(f"The total inventory value is {total}")    #Display the result


#Menu function
def menu():
    while True:
            print()
            print("-" * 40)
            print("     Inventory Management System :0")
            print("-" * 40)
            print("\nWelcoe to IMS below is the menu for this program")
            print("\n------Menu------")
            print("1.Add products to inventory")
            print("2.Consult products from inventory")
            print("3.Update product prices")
            print("4.DElete products from inventory")
            print("5.Calculate total value from inventory")
            print("6.Exit the program")

            option = input("\nChoose an option:")

            if option == "1":  #declare options with conditionals
                add_products()
        
            elif option == "2":
                consult_products()

            elif option == "3":
                update_prices()

            elif option == "4":
                delete_produts()
            
            elif option == "5":
                total_inventory_value()
            
            elif option == "6":
                print("\nThanks for using the program :)")
                break #program ends
            else:
                print("\nPlease enter a number beetwen 1-6")  #if user enter a number outside of those allowed

#Start program
menu()