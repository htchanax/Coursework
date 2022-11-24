# Assignment: Final Project - main execution file importing codes from other programs
# Shortcake Program - main execution program, importing shortcakes.py (class defining program)
# Description: Mrs.Bake owns a small bakery selling four different types of shortcakes, repeatedly-used business system built
# Learning Objectives: Creating two classes, applying inheritance and polymorphism

import shortcakes

def main():
    try:
        
        
        #instantiate the objects from two classes
        Shortcake1 = shortcakes.Shortcake(5.5,'famous',60)
        Shortcake2 = shortcakes.Shortcake(3.5,'lemon',40)    

        ShortcakeWithTopping1 = shortcakes.ShortcakeWithTopping(3.5,'blueberry',50,'buttercream')
        ShortcakeWithTopping2 = shortcakes.ShortcakeWithTopping(4.5,'chocolate', 30,'raspberry')
        ShortcakeWithTopping3 = shortcakes.ShortcakeWithTopping(6.5,'vanilla', 40,'raisin') 

        # append all the objects into the list
        list = [Shortcake1,Shortcake2,ShortcakeWithTopping1,ShortcakeWithTopping2,ShortcakeWithTopping3]


        #starting the while loop
        
        loop_again = 'yes'
        loop_again = loop_again.lower()
        while loop_again =='yes':

            #displaying the menu
            
            choice=display_menu()

            # menu-driven program
            
            if choice == 'P':
                target_object =getShortcake(list)
                if target_object !=0:
                    new_price = float(input('Please enter the new price for this flavor: '))

                    if new_price <0:
                        print('New price cannot be negative!')
                    else:
                        target_object.set_price(new_price)
                
            elif choice =='T':
                target_object = getShortcake(list)
                if target_object !=0:
                    new_topping = input('Please enter the new topping for this flavor: ')
                    if isinstance (target_object,shortcakes.ShortcakeWithTopping):
                        target_object.set_topping(new_topping)
                    else:
                        print('This cake does not have a topping!')


            elif choice =='R':
                print('Shortcake Report')
                print('==================')
                for item in list:
                    print(item)

            #initiating the startover of the loop        
            loop_again = input('\nDo you want to continue (yes or no)? ')
            loop_again = loop_again.lower()



     # General exception handling   
    except Exception as err:
        print(err)


# function 2: displaying the menu for the menu driven program      
def display_menu():
    print('Welcome to the Shortcake Menu')
    print('=============================')
    print('P-Set price')
    print('T-Set Topping')
    print('R-Print Report')
    print()
    
    choice = input('Please enter your selection: ')
    choice = choice.upper()
    while not (choice =='P'or choice =='T' or choice =='R'):
        choice = input('Invalid choice! Please enter your selection: ')
        choice = choice.upper()
    return choice

# function 3: required getShortcake program
def getShortcake(list):
    flavor = input('Which flavor of shortcake?')
    flavor = flavor.lower()
    count = 0
    for obj in list:
        searched_item = obj.get_flavor()
        if flavor == searched_item:
            print('The shortcake has been found!')
            print(obj)
            target = obj
         
        else:
            count = count+1

        if count == 5:
            target = 0
            print('The shortcake is not on the list!')
            
    return target
        
            
            

#calling the main function to execute    
main()
# Assignment: Final Project - Program of class (shortcakes.py) - defining class
# Shortcake Program - defining classes program
# Description: Mrs.Bake owns a small bakery selling four different types of shortcakes，repeatedly-used business system built
# Learning Objectives: Creating two classes, applying inheritance and polymorphism

# superclass program

class Shortcake:

    def __init__(self,price,flavor,inventory):
        self.__price = price
        self.__flavor = flavor
        self.__inventory = inventory

    def __str__(self):
        return '\nPrice is '+str(self.__price)+'\nFlavor is '+self.__flavor+'\nInventory is '+str(self.__inventory)+'\n'
    

    def set_price(self,price):
        self.__price = price

    def set_flavor(self,flavor):
        self.__flavor = flavor
        
    def set_inventory(self,inventory):
        self.__inventory = inventory

    def get_price(self):
        return self.__price
        
    def get_flavor(self):
        return self.__flavor
        
    def get_inventory(self):
        return self.__inventory




# subclass program


class ShortcakeWithTopping(Shortcake):

    def __init__(self,price,flavor,inventory,topping):
        Shortcake.__init__(self,price,flavor,inventory)
        self.__topping = topping

    def __str__(self):
        return Shortcake.__str__(self)+'Topping is '+self.__topping
    
    def set_topping(self,topping):
        self.__topping = topping

    def get_topping(self):
        return self.__topping
        

