#list comprehension = create new list with less syntax
    #list variable = [expression for item in iterable]
squares = []
for i in range(1,11):
    squares.append(i*i)
print (squares)

better_squares = [i*i for i in range(1,11)]
print(better_squares)
