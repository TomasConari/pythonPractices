#For


#String
quote = "Tomas"
print("For String: ")
for letter in quote:
    print(letter)

#List
example_list = [0, 5, 10, 15, 20, 25]
print("For List: ")
for num in example_list:
    print(num)

#Dictionary
example_dictionary = {
    "name":"Tomás",
    "lastname":"Contreras",
    "age":"19",
    "isAdult":True
}
print("For Dictionary Keys: ")
for key in example_dictionary:
    print(key) #In python when iterating over a dictionary, only the keys are received
print("For Dictionary Values: ")
for value in example_dictionary.values():
    print(value)
print("For full Dictionary: ")
for key, value in example_dictionary.items(): #In Python, during the iteration of a for loop, the unpacking process is based on the position and structure of the elements in the iterable
    print(f"{key}:{value}")

#Range
print("For in Range: ")
for i in range(10, 20, 2): #for range explication visit: "\range.py"
    print(i)


#While
    

counter = 1
print("While: ")
while counter <= 5:
    print(counter)
    counter += 1