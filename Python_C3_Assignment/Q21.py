# Python program to create a person class. Include attributes like name,
# country and date of birth. Implement a method to determine the person's age

from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    
    def calculate_age(self):
        today=date.today() # for getting today's date 2023-31-12
        age=today.year-self.dob.year 
        if today<date(today.year,self.dob.month,self.dob.date):
            age-=1
        return age
        

person1=Person("Ferdi Odilia", "France", date(1962, 7, 12))
person2=Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person3=Person("Elizaveta Tilman", "USA", date(2000, 1, 1)) 

print("Name:",person1.name)
print("Country",person1.country)
print("dob",person1.dob)
print("Age",person1.calculate_age())