# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:09:35 2017

@author: joelee
"""

inventory = {"Toluene":20,
             "Ammonium Nitrate":5, 
             "HMX":2
}
manage_system = "y"
while manage_system == "y":
# print (list(inventory["products"]))

    print (list(inventory.keys()))
    action = input ("Do you want to (a)dd | (r)emove | (d)isplay stock ")
    print (action)
    
    if action == "a" :
        newItem = input("what do you want to add?")
        print (newItem)
        
    elif action == "r" :
        delItem = input ("what do you want to remove")
        print (delItem)
        
    elif action == "d": 
        print ("Here is the current inventory")
    
manage_system = input("Would you like to continue working? (y)es or (n)o ")
    
