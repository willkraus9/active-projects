# zip(iterables) = combine elements from >=2 iterables (lists, tuples, sets,etc.)
    #creates zip object (new) in form of tuple
usernames = ['Mister','Dude','Bro']
passwords = ('p@ssword','abc223','guest')
#get both iterable in pairs
users = dict(zip(usernames,passwords))
for key,value in users.items():
    print(key+" : "+value)
