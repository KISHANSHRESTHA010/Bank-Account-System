
class Person:

    no_of_people=0

    def __init__(self,name):
        self.name=name
        Person.no_of_people+=1

    @classmethod  #<---THis is know as a decorator
    def number_of_People(cls):
        return cls.no_of_people#<----Unlike self this classmethod acts for the whole class not just one instance 

    @classmethod
    def add_people(cls):
        cls.no_of_people+=1

p1=Person("Timi")
print(Person.no_of_people)
p2=Person("John")
print(Person.no_of_people)

print(Person.number_of_People())