#If/Elif/Else


userAge = int(input("How old are you? in years: "))
if userAge > 115:
    print("You cannot enter a number greater than 115")
elif userAge < 0:
    print("You cant be under 0 years old")
elif userAge > 17:
    print("You are an adult")
else:
    print("You are not and adult")