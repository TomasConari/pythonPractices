#If/Elif/Else


user_age = int(input("How old are you? in years: "))
if user_age > 115:
    print("You cannot enter a number greater than 115")
elif user_age < 0:
    print("You cant be under 0 years old")
elif user_age > 17:
    print("You are an adult")
else:
    print("You are not and adult")