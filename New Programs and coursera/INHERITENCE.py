class Animal:
    def walk(self):
        print("animal is walking")

class Dog(Animal):
    def bark(self):
        print("woof woof")


class Cat(Animal):
    def meow(self):
        print("meow meow")

dog1=Dog()
dog1.walk()
dog1.bark()

cat1=Cat()
cat1.walk()
cat1.meow()


