#tuples = ordered + unchanging array; use arrays instead!

student = ("Bro", 21,"male")

print(student.count("Bro"))
    #counts how many times ___ appears
print(student.index("male"))
    #shows where in the tuple a value appears
    
for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here")