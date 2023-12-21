# Python program to find common items in two lists.

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]

# convert the lists into set and then use & for finding the common elements    
set_color1=set(color1)
set_color2=set(color2)
common=(set_color1 & set_color2)
print(common)