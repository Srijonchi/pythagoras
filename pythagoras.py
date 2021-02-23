import math
# Imports math from somewhere.
print("Please enter the values. \nNote: The hypotenuse value should be more than the known length value. ")
# Asks for user input (not using input)

# Pythagoras = a^2 + b^2 = c^2

while True:
    hypotenuse = int(input("Enter length of hypotenuse (in integer format, no units) here: "))    # Asks for hypotenuse input.
    known_length = int(input("Enter other known length (in integer format, no units) here: "))    # Asks for known length input.
    if hypotenuse > 0 and known_length > 0:    # Making sure that hypotenuse and known lenth are not negative and above 0.
        break    # Ends the loop once the values are positive.
# Looping if its negative until both values are more than 0.
# Also asks for user input for the two values.

if hypotenuse < known_length:    # Makes sure that hypotenuse is larger than the known length.
    print("The hypotenuse value should be higher than the known length value, please type in the numbers again.")    # Tells the user that their hypotenuse is less than their known length.
    hypotenuse = int(input("Enter length of hypotenuse (in integer format, no units) here: "))    # Asks for hypotenuse input again.
    known_length = int(input("Enter other known length (in integer format, no units) here: "))    # Asks for known length input again.
# This keeps looping until hypotenuse is larger than the known length.
else:    # Once a valid hypotenuse and known length input has been entered in executes following functions below.
    statement = "The unknown length is: "    # Prints the statement which is later added on to the final print statment.
    unknown_length1 = (hypotenuse * hypotenuse) - (known_length * known_length)    # Calculates the first step of the equation which does c^2 - b^2.
    unknown_length2 = str(math.sqrt(unknown_length1))    # Calculates the second step of the equation which square roots the answer using math.sqrt() and also converts the answer to a string using str() so that it can be used to print out.
    print(statement + unknown_length2)    # Finally prints out the final statement with the statement and the variable unknown_lenth2 to give an answer.