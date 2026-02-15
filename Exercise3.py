# Exercise 3: Normalize Phone Numbers
# The program takes a list of phone numbers in various formats and normalizes them to a standard
# format: '+380XXXXXXXXX'. The program should remove any non-numeric characters, ensure the country code is correct, and handle different input formats gracefully.
# BUT the program doesn't process the case where the number starts with country code that is not ukrainian, for example +380123456789 is correct, but +123456789 is not. 

import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)

    if cleaned_number.startswith('+'):
        return cleaned_number
    elif cleaned_number.startswith('380'):
        return '+' + cleaned_number
    else:
        return '+38' + cleaned_number
    

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("All normalised numbers for sms distribution:", sanitized_numbers)