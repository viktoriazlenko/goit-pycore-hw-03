# Exercise 1: Days from Today
# The program asks the user to input a date in the format 'YYYY-MM-DD' and then calculates how many days are left until that date from today. 
# If the date is in the past, it returns how many days have passed since that date. 
# If the input format is incorrect, it displays an error message.

import datetime

user_input = input("Type date at this format 'YYYY-MM-DD': ")

def get_days_from_today(user_input):
    try:
        input_date = datetime.datetime.strptime(user_input, '%Y-%m-%d') # Convert string to datetime object
        today = datetime.datetime.today()
        delta = input_date - today # Calculate the difference between the input date and today
        return delta.days
    except ValueError:
        return "Incorrect date format. Type date at this format 'YYYY-MM-DD'."
    
print(get_days_from_today(user_input))