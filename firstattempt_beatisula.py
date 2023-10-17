user_input = input("Enter your birth year: ")

if user_input.isdigit():
    birth_year = int(user_input)

    zodiac_sign = ""

    if birth_year % 12 == 0:
        zodiac_sign = "Monkey"
    elif birth_year % 12 == 1:
        zodiac_sign = "Rooster"
    elif birth_year % 12 == 2:
        zodiac_sign = "Dog"
    elif birth_year % 12 == 3:
        zodiac_sign = "Pig"
    elif birth_year % 12 == 4:
        zodiac_sign = "Rat"
    elif birth_year % 12 == 5:
        zodiac_sign = "Ox"
    elif birth_year % 12 == 6:
        zodiac_sign = "Tiger"
    elif birth_year % 12 == 7:
        zodiac_sign = "Rabbit"
    elif birth_year % 12 == 8:
        zodiac_sign = "Dragon"
    elif birth_year % 12 == 9:
        zodiac_sign = "Snake"
    elif birth_year % 12 == 10:
        zodiac_sign = "Horse"
    else:
        zodiac_sign = "Sheep"

    print(f"Your Chinese zodiac sign is the {zodiac_sign}.")
else:
    print("Invalid Input. Please enter a valid birth year as an integer.")
