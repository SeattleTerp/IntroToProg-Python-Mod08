# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2021,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# RKramer,5.31.2021,Modified IO Class with new methods
# RKramer,6.1.2021,Modified FileProcessor Class with new methods
# RKramer,6.1.2021,Imported Main script from assignment 06
# RKramer,6.1.2021,Modified Product Class for storage
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
# Declare variables and constants
file_name = "products.txt"  # The name of the data file
objFile = "products.txt"  # An object that represents a file
row = {}  # A row of data separated into elements of a dictionary {Product,Price}
list_of_rows = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strProduct = ""  # Captures the user product data
strPrice = ""  # Captures the user price data
strStatus = ""  # Captures the status of an processing functions
lstOfProductObjects = [] # A list that acts as a 'table' of rows

class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2021,Created Class
        RKramer,6.1.2021,Added fields, constructor, attributes and properties
    """
    # -- Fields --
    # Product =""
    # Price = ""

    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product = product_name
        self.__price = product_price

    # -- Properties --
    # product
    @property
    def product(self): # (getter or accessor)
        return str(self.__product).title() # Title case

    @product.setter
    def product(self, value): # (setter or mutator)
        try:
            if str(value).isnumeric() == False:
                self.__product = value
            else:
                raise Exception("Products cannot be numbers")
        except Exception as e:
            print("Prices can not be negative")
            print(e)
        return value

    # price
    @property
    def price(self):  # (getter or accessor)
        return str(self.__price).title()  # Title case

    @price.setter
    def price(self, value):  # (setter or mutator)
        try:
            if value >= 0:
                self.__price = value
            else:
                raise Exception("Prices cannot be negative")
        except Exception as e:
            print("Prices can not be negative")
            print(e)
        return value

    # -- Methods --
    def __str__(self):
        return self.__str__()

    def __str__(self):
        return self.product + ', ' + self.price
    # -- End of Class
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor(Product):
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2021,Created Class
        RKramer,6.1.2021,Modified code to complete assignment 8
    """
    @staticmethod
    def save_data_to_file(file_name, lstOfProductObjects):
        """ Writes product data from list of rows to file

        :param file_name: (string) with name of file being overwritten:
        :param lstOfProductObjects: (list) you read from to fill file:
        :return: (list) of dictionary rows
        """
        file = open(file_name, 'w')
        for row in lstOfProductObjects:
            file.write(row["Product"] + ", " + row["Price"] + "\n")
        file.close()
        return lstOfProductObjects, 'Success'

    @staticmethod
    def read_data_from_file(file_name, lstOfProductObjects):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        lstOfProductObjects.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            product_name, product_price = line.split(",")
            row = {"Product": product_name.strip(), "Price": product_price.strip()}
            lstOfProductObjects.append(row)
            pr = Product(product_name,product_price)
        file.close()
        return lstOfProductObjects, 'Success'

    @staticmethod
    def add_data_to_list(product_name, product_price, lstOfProductObjects):
        """ Adds data to a list of dictionary rows

        :param product_name: (string) with name of product:
        :param product_price: (string) with price:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = {"Product": str(product_name).strip(), "Price": str(product_price).strip()}
        lstOfProductObjects.append(row)
        return lstOfProductObjects, 'Success'

    def remove_data_from_list(product_to_remove, lstOfProductObjects):
        """ Removes product data and associated price from list of dictionary rows

        :param product_to_remove: (string) with name of product to be removed:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        for row in lstOfProductObjects:
            if row["Product"].lower() == product_to_remove.lower():
                lstOfProductObjects.remove(row)
                #print("row removed")
        return lstOfProductObjects, 'Success'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Processes data to and from a file and a list of product objects:

        methods:
            print_menu_Products():

            input_menu_choice(): -> (string)

            print_current_Products_in_list(lstOfProductObjects):

            input_yes_no_choice(message): -> (string)

            input_press_to_continue(optional_message=''):

            input_new_product_and_price(): -> (string)

            input_product_to_remove(): -> (string)

        changelog: (When,Who,What)
            RRoot,1.1.2021,Created Class
            RKramer,6.1.2021,Modified code to complete assignment 8
        """

    @staticmethod
    def print_menu_Products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Add a new Product
            2) Remove an existing Product
            3) Save Data to File        
            4) Reload Data from File
            5) Exit Program
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Products_in_list(lstOfProductObjects):
        """ Shows the current Products in the list of dictionaries rows

        :param lstOfProductObjects: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products are: *******")
        for row in lstOfProductObjects:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_price():
        """ Asks for new product and product's price

        :return: (strings) of product and price
        """
        product_name = str(input("Product:")).strip()
        product_price = str(input("Price:")).strip()
        return product_name, product_price

    @staticmethod
    def input_product_to_remove():
        """ Asks for product to remove

        :return: (strings) of product to remove
        """
        product_to_remove = str(input("Which product would you like to remove:")).strip()
        print()
        return product_to_remove

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Step 1 - read file data
FileProcessor.read_data_from_file(file_name, lstOfProductObjects)

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Products_in_list(lstOfProductObjects)  # Show current data in the list/table
    IO.print_menu_Products()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Product
        product_name, product_price = IO.input_new_product_and_price()
        FileProcessor.add_data_to_list(product_name, product_price, lstOfProductObjects)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Product
        product_to_remove = IO.input_product_to_remove()
        FileProcessor.remove_data_from_list(product_to_remove, lstOfProductObjects)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(file_name, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            FileProcessor.read_data_from_file(file_name, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
# Main Body of Script  ---------------------------------------------------- #