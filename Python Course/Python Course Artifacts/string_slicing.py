#slicing = create smaller string from larger string
    #index [] or slice() to create sliced object
    #for now, use index
#index [start:stop:step]

name = "Will Kraus"
first_name = name[:5]
print(first_name)
#just want first part of name; start at index 0, then exclude stopping index
    #NB: leaving first field blank assumes 0
    
last_name = name[5:]
    #NB: leaving second field blank asssumes rest of string
print(last_name)

funky_name = name[::2]
print(funky_name)

reversed_name = name[::-1]
    #just like counting backwards
print(reversed_name)

#slice object time

website1 = "http://google.com"
website2 = "http://wikipedia.com"
    #create substring that is just name of site
slice = slice(7,-4)
    #get string that accounts for diff lengths of website
    #negative index (char most on right = -1, etc.)
    #-4 index = end where .com begins
print(website2[slice])
