#Mathematical Operators

print("Mathematical Operators")

#Addition
addition = 5 + float(input("5 + "))
print(addition)

#Substraction
subtraction = 10 - float(input("10 - "))
print(subtraction)

#multiplication
multiplication = 2 * float(input("2 * "))
print(multiplication)

#division
division = 20 / float(input("20 / "))
print(division)

#integerDivision
integerDivision = 20 // float(input("20 // ")) #returns the result of the division discarding the decimals
print(integerDivision)

#modulo
modulo = 10 % float(input("10 % "))
print(modulo)

#exponentiation
exponentiation = 2 ** float(input("2 ** "))
print(exponentiation)


#Logical Operators

print("Logical Operators")

#And operator
bool1 = True
bool2 = True
comparison = bool1 and bool2
print(f"{bool1} and {bool2}: {comparison}")

#Or operator
bool1 = True
bool2 = False
comparison = bool1 or bool2
print(f"{bool1} or {bool2}: {comparison}")

#Not operator
bool1 = False
bool2 = False
comparison = not (bool1 and bool2)
print(f"not ({bool1} and {bool2}): {comparison}")


#Comparison Operators

print("Comparison Operators")

#Greater than
num = float(input("1 > "))
print((1 > num))

#Greater than or equal to
num = float(input("5 >= "))
print((5 >= num))

#Less than
num = float(input("3 < "))
print(3 < num)

#Less than or equal to
num = float(input("10 <= "))
print(10 <= num)

#Equal to
num = float(input("4 == "))
print(4 == num)

#Not equal to
num = float(input("4 != "))
print(4 != num)