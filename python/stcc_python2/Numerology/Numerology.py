# Nick Fernandes
# Python 2 Fall 2023
class Numerology:
    def __init__(self, name, birth_date):
        self.name = name.strip().upper()
        self.birth_date = birth_date.strip().replace('/', '-') # allows for / or - to be inputed

    def convert_to_number(self, character):
        conversion = {
            'A': 1, 'J': 1, 'S': 1,
            'B': 2, 'K': 2, 'T': 2,
            'C': 3, 'L': 3, 'U': 3,
            'D': 4, 'M': 4, 'V': 4,
            'E': 5, 'N': 5, 'W': 5,
            'F': 6, 'O': 6, 'X': 6,
            'G': 7, 'P': 7, 'Y': 7,
            'H': 8, 'Q': 8, 'Z': 8,
            'I': 9, 'R': 9
        }
        return conversion.get(character)

    """
    yeah not gonna lie got this function online lol
    but tldr is it takes a number and repeatedly sums its digits until it becomes a single-digit number and 
    if the input number is already a single digit it returns itself
    """
    def reduce_to_single_digit(self, number):
        if number < 10:
            return number
        else:
            digit_sum = sum(map(int,str(number)))
            return self.reduce_to_single_digit(digit_sum)

    def attitude_number(self):
        parts = self.birth_date.split('-')
        month = int(parts[0])
        day = int(parts[1])
        total = month + day
        return self.reduce_to_single_digit(total)


    def birth_day_number(self):
        day = int(self.birth_date.split('-')[1])
        return self.reduce_to_single_digit(day)

    def life_path_number(self):
        numbers = self.birth_date.replace('-', '')
        total = sum(map(int, numbers))
        return self.reduce_to_single_digit(total)

    def personality_number(self):
        total = 0
        for char in self.name:
            if char.isalpha() and char not in "AEIOU":
                total += self.convert_to_number(char)
        return self.reduce_to_single_digit(total)

    def soul_number(self):
        total = 0
        for char in self.name:
            if char in "AEIOU":
                total += self.convert_to_number(char)
        return self.reduce_to_single_digit(total)

    def power_name_number(self):
        return self.reduce_to_single_digit(self.soul_number() + self.personality_number())
