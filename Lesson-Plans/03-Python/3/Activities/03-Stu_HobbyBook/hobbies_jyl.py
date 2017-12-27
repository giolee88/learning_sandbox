# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:04:15 2017

@author: joelee
"""

## Info in Dictionaries

### Instructions

#* Create a dictionary that will store the following:

#  * Your name
#  * Your age
#  * A list of a few of your hobbies
#  * A dictionary of a few times you wake up during the week

#* Print out your name, how many hobbies you have and a time you get up during the week.

person = {
        "name": "Jack Reaper", 
        "age": 40,
        "hobbies": ["wrenching", "coding", "construction", "finding trouble"],
        "wake-times": {"weekdays":5, 
                       "weekends": 10,
                       "naps":16}
}

print ("Hello I am " + person["name"] )
print ("I can tell you about my ")
print (list(person.keys()))
print( "I have " + str(len(person["hobbies"])) + " Hobbies" )
print (list(person["hobbies"]))
hobbyList = ', '.join(map(str,person["hobbies"]))
print ("This includes " + hobbyList + ". ")

#for hobby in person["hobbies]: 
#    hobbyCommaList = hobbyCommaList + hobby
#    print (hobbyCommaList)
    
print (person["name"] + "'s work days start at " + str(person["wake-times"]["weekdays"]) + " o'clock")
# print (len(person["hobbies]))