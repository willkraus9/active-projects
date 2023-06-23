#map function = apply function to each item in iterable
    #accept function, iterable

store = [('shirt',20.00),
         ('pants',25.00),
         ('jacket',50.00),
         ('socks',10.00),]
#convert price to euros: 1USD = 0.82 Euros
to_euros = lambda data: (data[0], data[1]*0.82)
to_dollars = lambda data: (data[0], data[1]/0.82)
store_euros = list(map(to_euros,store))
store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)