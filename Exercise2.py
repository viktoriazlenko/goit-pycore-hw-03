# Exercise 2: Lottery Ticket Generator  
# The program generates a lottery ticket with a specified number of unique random numbers within a given range. 
# The user can specify the minimum and maximum values for the numbers, as well as how many numbers should be on the ticket. 
# The program should validate the input parameters and ensure that the quantity of numbers requested does not exceed the range of possible unique numbers. 
# If the parameters are valid, it returns a sorted list of unique random numbers. If the parameters are invalid, it returns an empty list.

import random

def get_numbers_ticket(min, max, quantity):
    
    if min >= 1 and max <= 1000 and quantity > 0 and quantity <= (max - min + 1):  # Validate input parameters
        numbers = set()
        while len(numbers) < quantity: 
            numbers.add(random.randint(min, max)) # Generate unique random numbers until the desired quantity is reached
        return sorted(numbers)
    
    else:
        return [] # Return an empty list if parameters are out of bounds, but do not raise an error that I'd improve in the future, but I want to align with the requiements. 
    

# For negative scenario: lottery_numbers = get_numbers_ticket(100000000, -1, 6)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)


