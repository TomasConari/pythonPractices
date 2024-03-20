#In this simple assignment you are given a number and have to make it negative. 
#But maybe the number is already negative?

#https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python

num = int(input("Enter a number "))

def make_negative(number):
    if number > 0:
        return number * -1
    else:
        return number
    
print(make_negative(num))