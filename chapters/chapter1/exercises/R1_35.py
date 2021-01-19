# without counting leap year adjustments
# nnot sure whether below is the solution author intended

import random


birthdays = []
same_birthday_flag = False

# n is number of people
for n in range(5, 101):
    same_birthday_flag = False
    birthdays = []
    # generate random days of a year - n number of birthdays
    for i in range(n):
        birthday = random.randint(1,366)
        if birthday in birthdays:
            same_birthday_flag = True
            break
        birthdays.append(birthday)
    print("For n = {0}, whether two people had".format(n),
          "same bithday = {0}".format(same_birthday_flag))
    
    
    
