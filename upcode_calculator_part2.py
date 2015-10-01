from arithmetic import *  # stars means everything or wild card

#Exercise: Calcualtor, Part 2: The REPL
#using REPL and using Tokens

#Concepts Required

    #  functions
    #  arithmetic
    #  return values
    #  string parsing
    #  conditionals


# No setup
#repeat forever:
    #read input
    #tokenize input
    #if the first token is 'q', quit
    #otherwise decide which math function to call based on the tokens we read
"""
upcode_calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
print "Lengendary Calcualtor"
# While loop
while True:
    user_input = raw_input(">")
    token = user_input.split(" ")
    if token[0] == "+" or token[0] == "add":
        print (add(token[1], token[2]))
    elif token[0] == "-" or token[0] == "sub" or token[0] == "subtract":
        print (subtract(token[1], token[2]))
    elif token[0] == "*" or token[0] == "multiply" or token[0] == "mult":
        print (multiply(token[1], token[2]))
    elif token[0] == "/" or token[0] == "divide":
        print (divide(token[1], token[2]))
    elif token[0] == "square":
        print (square(token[1]))
    elif token[0] == "cube":
        print (cube(token[1]))
    elif token[0] == "pow" or token[0] == "**" or token[0] == "power":
        print (power(token[1], token[2]))
    elif token[0] == "mod" or token[0] == "%":
        print (mod(token[1], token[2]))
    elif token[0] == "q":
        print "winner chicken dinner"
        break  # ends loop
    else:
        print "Try again"
        print "arithmetic, number(s)"
        print "ex: + 3 4"
