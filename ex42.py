from textwrap import dedent

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


## ?? Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ?? Dog is-a Animal, has-a name
        self.name = name


## ?? Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## ?? Cat is-a Animal has-a name
        self.name = name


## ?? Person is-a object
class Person(object):

    def __init__(self, name):
        ## ?? Person has-a name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None


## ?? Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee is-a Person has-a name - hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee is-a Person has-a salary
        self.salary = salary


## ?? Fish is-a object
class Fish(object):
    pass


## ?? Salmon is-a Fish
class Salmon(Fish):
    pass


## ?? Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a a Dog - Dog has-a name"Rover"?
rover = Dog("Rover")

## ?? satan is a Cat has-a name
satan = Cat("Satan")

## ?? mary is-a Person has-a name
mary = Person("Mary")

## ?? mary has-a pet is-a satan? or mary has-a satan is-a pet?
mary.pet = satan

## ?? frank is-a Employee has-a name and salary
frank = Employee("Frank", 120000)

## ?? frank has-a pet is-a rover? or frank has-a satan is-a pet?
frank.pet = rover

## ?? flipper is-a Fish
flipper = Fish()

## ?? crouse is-a Salmon
crouse = Salmon()

## ?? harry is-a a Halibut
harry = Halibut()


class Garden(object):

    def __init__(self, pet_names):
        pet1 = Dog(pet_names[0])
        pet2 = Cat(pet_names[1])
        self.pets = [pet1, pet2]
        self.car = None


garden = Garden(["bob", "lola"])
print([pet.name for pet in garden.pets])
print(garden.pets)
print("\n")
print(Garden(["joe", "kly"]))

def corgi1():
    print("""                        corgicorgicorgicorgicorgicorgicor
          gicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgico
          rgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgi
          corgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgi""")


def corgi2():
    print(dedent("""                 corgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicor"
                 gicorgicorgicorgicorgicorg"
                 icorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgicorgi"""))

corgi1()
print("\n")
corgi2()