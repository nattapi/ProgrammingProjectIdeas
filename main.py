import random
import string

length = input("Enter password length: \n")
symbols = input("Include symbols? (e.g. @#$%) Enter y=Yes or n=No \n")
numbers = input("Include symbols? (e.g. 123456) Enter y=Yes or n=No \n")
lower_case = input("Include lowercase characters? Enter y=Yes or n=No \n")
upper_case = input("Include uppercase characters? Enter y=Yes or n=No \n")

if symbols == 'y' and numbers == 'n' and lower_case == 'n' and upper_case == 'n': 
    x = range(int(length))
    password = list()
    for n in x:
        password.append(random.choice(string.punctuation))
        print(password)
    print("".join(password))
