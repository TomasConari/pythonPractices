#Try/Except/Finally


try:
    result = 100.0 / float(input("Enter a number by which to divide 100: "))
    print(f"Result: {result}")
except Exception as newError:
    print(f"Error: {newError}")
finally:
    print("Program completed") #Finally always Executes