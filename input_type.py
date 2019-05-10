name = raw_input("What's your name? ")
print("Nice to meet you " + name + "!")
age = raw_input("Your age? ")
print("So, you are already " + str(age) + " years old, " + name + "!")

#The input of the user will be interpreted. If the user e.g. puts in an integer value, the input function returns this integer value. If the user on the other hand inputs a list, the function will return a list. Python takes your name as a variable. So, the error message makes sense! 

#raw_input does not interpret the input. It always returns the input of the user without changes, i.e. raw. This raw input can be changed into the data type needed for the algorithm. To accomplish this we can use either a casting function or the eval function
