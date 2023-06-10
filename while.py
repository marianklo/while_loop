# The program will always asks the user to enter a number.
# When the user enters -1, the program should stop requesting the user to enter a number,
# The program will then calculate the average of the numbers entered, excluding the -1.


# Create 2 variable, one for total numbers and one for counting the numbers

total = 0
count = 0
 
# Continuously asking user to input a number until they input -1
user_input = int(input("Please enter a number (-1 to exit) : "))
while user_input != -1 :
    total += user_input
    count += 1
    user_input = int(input("Please enter a number (-1 to exit) : "))

    if user_input == -1 :
        # Calcutaing the average when number -1 in input
        average = total / count
        print (f"The average of {count} entered numbers is {average:.2f}")