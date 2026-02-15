import datetime

user_input = input("Type date at this format 'YYYY-MM-DD': ")

def get_days_from_today(user_input):
    try:
        input_date = datetime.datetime.strptime(user_input, '%Y-%m-%d')
        today = datetime.datetime.today()
        delta = input_date - today
        return delta.days
    except ValueError:
        return "Incorrect date format. Type date at this format 'YYYY-MM-DD'."
    
print(get_days_from_today(user_input))