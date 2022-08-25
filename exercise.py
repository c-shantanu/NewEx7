from curses.ascii import isupper


user_string = input("Enter your string: ")

if user_string.islower():
    print(user_string.upper())

elif user_string.isupper():
    print(user_string.lower())

