#Complete the method that takes a boolean value and return a "Yes" string for true, 
#or a "No" string for false.

#https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python

inputBoolean = int(input("1. True \n2. False\n"))
if inputBoolean == 1:
    inputBoolean = True
else:
    inputBoolean = False

def boolToWord(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
print(boolToWord(inputBoolean))


