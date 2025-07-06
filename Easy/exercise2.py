# """Exercise 2
# Ask the user for a number. 
# Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message."""

nb=int(input("Please enter a number: "))
if nb % 2==0:
    print(f"The number {nb} is even.")
elif nb % 4==0:
    print(f"The number {nb} is a multiple of 4.")      
else:
    print(f"The number {nb} is odd.")
  
check = int(input("Enter a number to divide by: "))

if nb % check == 0:
    print(f"{check} divides evenly into {nb}.")
else: 
    print(f"{check} does not divide evenly into {nb}.")    
    