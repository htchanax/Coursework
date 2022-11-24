# Name: Hiu Tung Chan (Veronica),Amy Cox
# Assignment: Final Project - Program of class (shortcakes.py)
# Date: 5/12/2019
# Section: 9:30-11:00

# Part1 - Shortcake Program(60%) - defining classes program
# Description: Mrs.Bake owns a small bakery selling four different types of shortcakes
# She would like to have a repeatedly-used business system built

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
        
