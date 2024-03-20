#Complete the method that takes a boolean value and return a "Yes" string for true, 
#or a "No" string for false.

#https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python

input_boolean = int(input("1. True \n2. False\n"))
if input_boolean == 1:
    input_boolean = True
else:
    input_boolean = False

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
print(bool_to_word(input_boolean))


