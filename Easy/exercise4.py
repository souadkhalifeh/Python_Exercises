# Exercise 4: Ordered List Search
# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list 
# and returns (then prints) an appropriate boolean.

def is_number_in_list(ordered_list, number):
    """Check if a number is in an ordered list."""
    return number in ordered_list


ordered_list = [1, 3, 5, 7, 9, 11]
number = 5
result= is_number_in_list(ordered_list, number)
print(f"Is the number {number} in the list {ordered_list}? {result}")
