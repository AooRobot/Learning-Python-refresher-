# Pyhton walkthrough
# 1. Variables
# string boolean numbers
from math import *
character_name = "Alex"
character_gender = "Female"
characer_age = 24
is_new_char = False
phrase_string = "This the first time create a character"




# This is the main function
if __name__ == "__main__":
     print("Create character : " + character_name)
     print("Gender : " + character_gender)
    #  sting function like lower ,upper islower isupper
     print(character_name.lower().islower())
    #  len(string)
     print(len(phrase_string))
    #  string can be manipulated by using index
     print(phrase_string[0]) 
    #  string.index() return the index of a character or word
     print(phrase_string.index("first"))
    #  string.replace()
     print(phrase_string.replace("This","THis"))
    #  % mod 
     print(10 % 3)
    #  abs aboulute abs(-3) = 3
    # pow(3,2) = 9  3 power 2
    # max(4,6) find the max number min(4,6)
    # round(4.7) --> 5 round(4.3) --> 4
     print(ceil(3.7)) #  round up no matter what
     print(floor(3.7)) # chop off the decimal point
     print(sqrt(36)) # sqrt root = 
     print("-----------------------------------")
     set_points = input("please set your points: ")
     print("The points you have set: " + set_points)