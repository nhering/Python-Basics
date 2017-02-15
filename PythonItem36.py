# -*- coding: cp1252 -*-
# Python    2.7.13
#
# Author    Nathan Hering
#
# Purpose   The Tech Academy - Python course item 36

import math

'''
x 1. Assign an integer to a variable
x 2. Assign a string to a variable
x 3. Assign a float to a variable
x 4. Use the print function and .format() notation to print out the variable you assigned  
x 5. Use each of these operators +, - , * , / , +=, ­= , %
x 6. Use of logical operators: and, or, not
x 7. Use of conditional statements: if, elif, else
x 8. Use of a while loop
x 9. Use of a for loop
x 10. Create a list and iterate through that list using a for loop to print each item out on a new line
x 11. Create a tuple and iterate through it using a for loop to print each item out on a new line
x 12. Define a function that returns a string variable
x 13. Call the function you defined above and print the result to the shell
'''

def start(name=""):
    name = raw_input("What is your name?  ").capitalize()
    printName(name)
    yourInteger = 0
    yourFloat = 0
    number = 0
    getNumbers(yourInteger,yourFloat,number)

def printName(name):
    print("Hello {}.".format(name))

def getNumbers(yourInteger,yourFloat,number):
    if(yourInteger==0 and yourFloat==0):
        print ("\nyourInteger = {}".format(yourInteger))
        print ("yourFloat = {}".format(yourFloat))
        number = raw_input("\nEnter an integer or float. ")
        checkNumber(yourInteger,yourFloat,number)
    if(yourFloat==0):
        print ("\nyourInteger = {}".format(yourInteger))
        print ("yourFloat = {}".format(yourFloat))
        number = raw_input("\nNow select a float. ")
        checkNumber(yourInteger,yourFloat,number)
    elif(yourInteger==0):
        print ("\nyourInteger = {}".format(yourInteger))
        print ("yourFloat = {}".format(yourFloat))
        number = raw_input("\nNow select an integer. ")
        checkNumber(yourInteger,yourFloat,number)
    else:
        doMath(yourInteger,yourFloat)

def checkNumber(yourInteger,yourFloat,number):
    if (float(number)%1 == 0):
        print("We'll store {} as the integer 'yourInteger'".format(number))
        yourInteger = number
        getNumbers(yourInteger,yourFloat,number)
    else:
        print("We'll store {} as the float 'yourFloat'".format(number))
        yourFloat = number
        getNumbers(yourInteger,yourFloat,number)

mathSymbols = ("+","-","*","/","%");
mathAnswers = [];

def doMath(yourInteger,yourFloat):
    i = 0
    print("\nNow we'll take those numbers and perform the following opperations with them:\n")
    for item in mathSymbols:
        print item
    print
    while(i<len(mathSymbols)):
      if(mathSymbols[i] == "+"):
          result = int(yourInteger) + float(yourFloat)
          print("{} {} {} = {}".format(yourInteger,mathSymbols[i],yourFloat,result))
          mathAnswers.append(result)
          i+=1
      if(mathSymbols[i] == "-"):
          result = int(yourInteger) - float(yourFloat)
          print("{} {} {} = {}".format(yourInteger,mathSymbols[i],yourFloat,result))
          mathAnswers.append(result)
          i+=1
      if(mathSymbols[i] == "*"):
          result = int(yourInteger) * float(yourFloat)
          print("{} {} {} = {}".format(yourInteger,mathSymbols[i],yourFloat,result))
          mathAnswers.append(result)
          i+=1
      if(mathSymbols[i] == "/"):
          result = int(yourInteger) / float(yourFloat)
          print("{} {} {} = {}".format(yourInteger,mathSymbols[i],yourFloat,result))
          mathAnswers.append(result)
          i+=1
      if(mathSymbols[i] == "%"):
          result = int(yourInteger) % float(yourFloat)
          print("{} {} {} = {}".format(yourInteger,mathSymbols[i],yourFloat,result))
          mathAnswers.append(result)
          i+=1
    printAnswers(yourInteger,yourFloat)


def printAnswers(yourInteger,yourFloat):
    print("\nNow lets look at just the answers.")
    for item in mathAnswers:
        print item
    logicalOperators(yourInteger,yourFloat)

def logicalOperators(yourInteger,yourFloat):
    print("\nLet's do a few logical opperators.")
    print("\nAre your integer({}) AND your float({}) greater than 10?").format(yourInteger,yourFloat)
    print(int(yourInteger)>10 and float(yourFloat)>10)
    print("\nAre either your integer({}) OR your float({}) less than 10?").format(yourInteger,yourFloat)
    print(int(yourInteger)<10 or float(yourFloat)<10)
    print("\nThe following statement is")
    print(1 == 1)
    print("The previous statement was")
    print not(1 == 1)
    exit()



    

if __name__ == "__main__":
    start()
