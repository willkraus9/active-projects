#reduce = applies function to iterable, creates 1 cumulative value
    #first two elements, execute function, result = 1 variable
import functools

letters = ['H','E','L','L','O']
word = functools.reduce(lambda x,y: x+y,letters)
print(word)

factorial = [5,4,3,2,1]
number = functools.reduce(lambda x,y: x+y,factorial)
print(number)