# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:10:22 2017

@author: joelee
"""

sourceWord = input ("give me a word here: ")
print (sourceWord)

shiftNumber = int(input("shift number? "))


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]

letters = list(sourceWord)
print (letters)
for letter in letters:
    pos=alphabet.index(letter)
    cipherPos=alphabet.index(letter)+3
    print (str(pos) + str(cipherPos))
    print (len(alphabet))


