# Rachel Ring
# 08/03/2021

# display a menu function
def display_menu():
    print("*" * 32)
    print("{:<1}{:^30}{:>1}".format("*", "Computer Supplies System", "*"))
    print("*" * 32)
    print("\t1- List All Products")
    print("\t2- List Low Stock Products")
    print("\t3- Print Product Profits")
    print("\t4- Total Stock Value")
    print("\t5- Exit")
    print("*" * 32)


# option 1 - display all product details
def display_products(product_lst_in):
    print("*" * 95)
    print("{:<1}{:^93}{:>1}".format("*", "Product Details", "*"))
    print("*" * 95)
    print("{:15}{:20}{:15}{:15}{:15}{:15}".format("Product ID", "Name", "Selling Price", "Cost Price",
                                                  "Quantity", "Re-order Level"))
    print("*" * 95)
    for product in product_lst_in:
        for i, info in enumerate(product):
            if i == 1:
                print("{:<20}".format(info), end="")
            else:
                print("{:<15}".format(info), end="")
        print()


# option 2 - display all products that have low stock levels
def list_low_stock(product_lst_in):
    print("*" * 65)
    print("{:<1}{:^63}{:>1}".format("*", "Low Stock Products", "*"))
    print("*" * 65)
    print("{:15}{:20}{:15}{:15}".format("Product ID", "Name", "Quantity", "Re-order Level"))
    print("*" * 65)
    for i, row in enumerate(product_lst_in):
        if product_lst_in[i][4] <= product_lst_in[i][5]:
            for j, info in enumerate(row):
                if j == 0 or j == 4 or j == 5:
                    print("{:<15}".format(info), end="")
                elif j == 1:
                    print("{:<20}".format(info), end="")
            print()


# option 3 - display profit margin for each product
def calculate_profit(product_lst_in):
    print("*" * 80)
    print("{:<1}{:^78}{:>1}".format("*", "Product Details", "*"))
    print("*" * 80)
    print("{:15}{:20}{:15}{:15}{:15}".format("Product ID", "Name", "Selling Price", "Cost Price",
                                             "Profit"))
    print("*" * 80)
    for i, product in enumerate(product_lst_in):
        for j, info in enumerate(product):
            if j == 1:
                print("{:<20}".format(info), end="")
            elif j == 0 or j == 2 or j == 3:
                print("{:<15}".format(info), end="")
        print("{:<15}".format(round(product_lst_in[i][2] - product_lst_in[i][3], 2)))


# option 4 - display stock value for the company
def calculate_stock_value(product_lst_in):
    totals = []
    for i, row in enumerate(product_lst_in):
        product_total_value = product_lst_in[i][2] * product_lst_in[i][4]
        totals.append(product_total_value)
    stock_value = sum(totals)
    print("*" * 40)
    print("{:^40}".format("Total Stock Value €"+str(stock_value)))
    print("*" * 40)


product_list = [["CS567", "Wireless Printer", 49.99, 20.00, 8, 10],
                ["CS100", "Document Scanner", 109.99, 60.00, 11, 5],
                ["CS777", "Ink Cartridge", 29.99, 15.00, 12, 25],
                ["CS800", "Full HD Webcam", 64.00, 30.00, 12, 10],
                ["CS990", "Optical Mouse", 5.99, 2.00, 10, 5]]
display_menu()
menu_option = int(input("Please Enter option:\t"))
while menu_option != 5:
    if menu_option == 1:
        display_products(product_list)
        display_menu()
        menu_option = int(input("Please Enter option:\t"))
    elif menu_option == 2:
        list_low_stock(product_list)
        display_menu()
        menu_option = int(input("Please Enter option:\t"))
    elif menu_option == 3:
        calculate_profit(product_list)
        display_menu()
        menu_option = int(input("Please Enter option:\t"))
    elif menu_option == 4:
        calculate_stock_value(product_list)
        display_menu()
        menu_option = int(input("Please Enter option:\t"))
    else:
        print("!ERROR!\n\tPlease enter a valid menu option\n\t1, 2, 3, 4, or 5")
        display_menu()
        menu_option = int(input("Please Enter option:\t"))
