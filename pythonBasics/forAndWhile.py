quote = "Tomas"
print("For String: ")
for letter in quote:
    print(letter)


exampleList = [0, 5, 10, 15, 20, 25]
print("For List: ")
for num in exampleList:
    print(num)


exampleDictionary = {
    "name":"Tomás",
    "lastname":"Contreras",
    "age":"19",
    "isAdult":True
}
print("For Dictionary Keys: ")
for key in exampleDictionary:
    print(key) #In python when iterating over a dictionary, only the keys are received
print("For Dictionary Values: ")
for value in exampleDictionary.values():
    print(value)
print("For full Dictionary: ")
for key, value in exampleDictionary.items(): #In Python, during the iteration of a for loop, the unpacking process is based on the position and structure of the elements in the iterable
    print(f"{key}:{value}")


print("For in Range: ")
for i in range(10, 20, 2): #for range explication visit: "\range.py"
    print(i)


counter = 1
print("While: ")
while counter <= 5:
    print(counter)
    counter += 1