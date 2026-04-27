#password generator
import random
import string
print("------Welcome to password generator------")
length_in = input("Enter length of your password ? : ")
if length_in.isdigit() == False:
    print("Only integers are allowed.")
else:
    length=int(length_in)
    if length <= 0:
        print("Please enter a valid length.")
    else:
        all_chars = string.ascii_letters + string.digits + "@#$&*!"
        password = ""
        for i in range(length):
            selected_char = random.choice(all_chars)
            password = password + selected_char
        print("\nYour password is :", password)
