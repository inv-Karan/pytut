class NameOfClass():
    def __init__(self,param1,param2):
        self.param1=param1
        self.param2=param2

    def some_method(self):
        #perform some action
        print(self.param1)
    
    def some_method(self):
        #perform some action
        print(self.param2)

mylist = [1,2,3]
myset = set()
print(type(myset))
print(type(mylist))

class Sample():
    pass

my_sample = Sample()
print(type(my_sample))

class Dog():

    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self,breed,mybreed,name,spots):
        #super().__init__()
        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.name = name
        #Expect boolean True/False
        self.spots = spots

        self.breed = breed
        my_dog = Dog(breed='Lab')
        print(type(my_dog))
        print(my_dog.breed)

        self.mybreed = mybreed
        my_dog = Dog(mybreed='Huskie')
        print(type(my_dog))
        print(my_dog.mybreed)

        self.my_attribute = mybreed
        my_dog = Dog(mybreed='Dober')
        print(type(my_dog))
        print(my_dog.mybreed)

        self.my_attribute = breed
        my_dog = Dog(breed='pom')
        print(type(my_dog))
        print(my_dog.my_attribute)

        my_dog = Dog(breed='Lab',name='Sammy',spots=False)
        print(my_dog.breed)
        print(my_dog.name)
        print(my_dog.spots)
        print(my_dog.species)

        #OPERATIONS/Actions--->Methods
        def bark(self,number):
            print("WOOF!")
            print(my_dog.bark())
            print("WOOF! My name is {} and the number is {}".format(self.name,number))
            print(my_dog.bark(10))

class Circle():

    #CLASS OBJECT ATTRIBUTE
    
    pi = 3.14
    my_circle = Circle()
    print(my_circle.pi)
    
    def __init__(self,radius=1):
        #super().__init__()
        self.radius = radius
        print(my_circle.radius)
        self.area = radius * radius * self.pi
        print(my_circle.area)
        self.area = radius * radius * Circle.pi
        print(my_circle.area)

    
    #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2
        print(my_circle.get_circumference())
        #return Circle.radius * Circle.pi * 2
        #print(my_circle.get_circumference())

#INHERITANCE

class Animal():
    def __init__(self):
        #super().__init__()
        print("ANIMAL CREATED")

        my_animal = Animal()

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

        my_dog = Dog()
        print(my_dog.eat())

    def who_am_i(self):
        print("I am a dog")

        my_dog = Dog()
        print(my_dog.who_am_i())

    def bark(self):
        print("WOOF!")

        my_dog = Dog()
        print(my_dog.bark())

    def eat(self):
        print("I am a dog and eating")

        my_dog = Dog()
        print(my_dog.eat())

#POLYMORPHISM

class Dog():

    def __init__(self,name):
        #super().__init__()
        self.name = name

    def speak(self):
        return self.name + " says woof"

        niko = Dog("niko")
        print(niko.speak())

        for pet in [niko]:
            print(type(pet))
            print(type(pet.speak()))

    def pet_speak(self):
        print(self.speak())

class Cat():

    def __init__(self,name):
        #super().__init__()
        self.name = name

    def speak(self):
        return self.name + " says meow"

        felix = Cat("felix")
        print(felix.speak())

        for pet in [felix]:
            print(type(pet))
            print(type(pet.speak()))

    def pet_speak(self):
        print(self.speak())

class Animal():

    def __init__(self,name):
        #super().__init__()
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

        myanimal = Animal('fred')
        print(myanimal.speak()) #throws error mentioned above

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"

        fido = Dog("Fido")
        print(fido.speak())


class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"

        isis = Cat("Isis")
        print(isis.speak())

#SPECIAL METHODS

mylist = [1,2,3]
print(len(mylist))

class Sample():
    pass
    mysample = Sample()
    print(mysample)
    print(mylist)

class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

        b = Book('Python Rocks','Jose',200)
        print(b)

        print(str(b))

    def __str__(self):
        #return super().__str__()
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages()
        print(len(b))

    def __del__(self):
        print("A book object has been deleted")