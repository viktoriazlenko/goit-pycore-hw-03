# Exercise 4: Upcoming Birthdays
# The program takes a list of users with their names and birthdays. 
# It checks which users have birthdays in the upcoming week and returns a list of those users along with the date they should be congratulated. 
# If a user's birthday falls on a weekend, the program should suggest congratulating them on the following Monday. 


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Bob Brown", "birthday": "1992.04.25"},
    {"name": "Alice Green", "birthday": "1995.02.22"},
    {"name": "Charlie Black", "birthday": "1988.02.21"},
    {"name": "Emily White", "birthday": "1993.02.24"},
    {"name": "David Gray", "birthday": "1991.02.28"},
    {"name": "Olivia Blue", "birthday": "1994.02.17"}
]
    
from datetime import datetime, timedelta


def get_upcoming_birthdays(users):

    today = datetime.today().date()
    upcoming = []

    for user in users:
        obj_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # Convert string to date object
        birthday_this_year = obj_date.replace(year=today.year) # Set the birthday to the current year

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  # If the birthday has already passed this year, set it to next year

        days_difference = (birthday_this_year - today).days

        if 0 <= days_difference <= 7:
            this_week_birthday = birthday_this_year
            if this_week_birthday.weekday() >= 5:  # If birthday falls on Saturday (5) or Sunday (6)
                this_week_birthday += timedelta(days=(7 - this_week_birthday.weekday()))  # Move to next Monday

            upcoming.append({
                "name": user["name"],
                "congratulation_date": this_week_birthday.strftime("%Y.%m.%d") 
            })
    return upcoming

print("List of upcoming birthdays:", get_upcoming_birthdays(users))
