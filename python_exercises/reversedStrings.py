#Complete the solution so that it reverses the string passed into it.

#https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python

quote = input("Enter a word: ")

def solution(string):
    return string[::-1] #the expression "[::-1]" returns the string reversed

print(solution(quote))