# Password validator
# Nick Fernandes

def main():
    special_chars = ['!', '@', '#', '$', '%', '^']

    # get name 
    s_name = input("Please enter your first and last name: ")
    first_name, last_name = s_name.split()
    first_initial = first_name[0]
    last_initial = last_name[0]
    s_initials = first_initial + last_initial

    # ask for pw 
    s_password = input("Please enter your desired password: ")

    valid_password = True

    # verify len 8-12
    if not 8 <= len(s_password) <= 12:
        print("Password must be between 8 and 12 characters")
        valid_password = False

    # check for pass
    if "pass" in s_password.lower():
        print("Password cannot contain PASS or pass")
        valid_password = False

    # check 1 cap A-Z
    if not any(char.isupper() for char in s_password):
        print("Password must contain at least 1 uppercase letter.")
        valid_password = False

    # check 1 lower-case a-z
    if not any(char.islower() for char in s_password):
        print("Password must contain at least 1 lowercase letter.")
        valid_password = False

    # check 1 num 0-9
    if not any(char.isdigit() for char in s_password):
        print("Password must contain at least 1 number.")
        valid_password = False

    # check 1 special char. ! @ # $ % ^
    if not set(special_chars) & set(s_password):
        print("Password must contain at least 1 of these special characters ! @ # $ % ^.")
        valid_password = False

    # does not contain 
    if s_initials.lower() in s_password.lower():
        print(f"Password cannot contain the initials {s_initials}")
        valid_password = False

    # check occurrences
    char_dict = {}
    for char in s_password:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    repeated_chars={}
    for char, count in char_dict.items():
        if count > 1:
            repeated_chars[char] = count
    if repeated_chars:
        print("These characters appear more than once:")
        for char, count in repeated_chars.items():
            print(f"'{char}' appears {count} times")
        valid_password = False

    if valid_password:
        print("Password is valid and OK to use.")

main()
