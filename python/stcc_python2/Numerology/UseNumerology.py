# Nick Fernandes
# Python 2 Fall 2023
from Numerology import Numerology
def validate_date(date):
    # validate the birth date format and range.
    date = date.replace('/', '-')  # allows for / or - to be inputed
    try:
        parts = date.split('-')
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])

        if month >= 1 and month <= 12 and day >= 1 and day <= 31:
            return True
        else:
            return False

    except ValueError:
        return False

def main():
    name = input("Enter your name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    birth_date = input("Enter your birth date: ").strip()

    while not validate_date(birth_date):
        print("Invalid date, enter a valid date.")
        birth_date = input("Enter your birth date: ").strip()

    numerology = Numerology(name, birth_date)

    print("Life Path Number:", numerology.life_path_number())
    print("Birth Day Number:", numerology.birth_day_number())
    print("Attitude Number:", numerology.attitude_number())
    print("Soul Number:", numerology.soul_number())
    print("Personality Number:", numerology.personality_number())
    print("Power Name Number:", numerology.power_name_number())

main()
