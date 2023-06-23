#sort method = use with list
#sort function = use with iterables
students = ["Squidward",'Sandy','Patrick','Spongebob','Mr. Krabs']
    #only works with lists [], not tuples ()
students.sort() #alphabetical order
#students.sort(reverse = True) #reverse alphabetical order
#for i in students:
#    print(i)

#orted_students = sorted(students)
    #sorted = returns list
#for i in sorted_students:
#    print(i)

student_record = [('Squidward','F',60),
                  ('Sandy','A',33),
                  ('Patrick','D',36),
                  ('Spongebob','B',20),
                  ('Mr. Krabs','C',78)]
#sort by grade, age, or name
grade = lambda grades:grades[1]
age = lambda grades:grades[2]
student_record.sort(key = age, reverse=True)
for i in student_record:
    print(i)

    
