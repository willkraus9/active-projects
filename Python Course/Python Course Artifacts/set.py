#set = collection unordered, unindexed (no duplicate values)
    #use curly braces (arrays = brackets, tuples = parentheses)
utensils = {"fork","spoon","knife"}
for x in utensils:
    print(x)

utensils.add("napkin")
utensils.remove("fork")
#add item

dishes = {"Bowl", "Plate", "Cup"}
utensils.update(dishes)
    #add all elements within dishes to utensils
for x in dishes:
    print(x)

dinner_table = utensils.union(dishes)
    #puts two sets together under new name
    
print(utensils.difference(dishes))  
    #prints what utensils has but dishes doesn't
print(utensils.intersection(dishes))
    #prints what utensils and dishes both have