class Person:
    def __init__(self, name):
        self.name = name  # constructor to initialize name

    def talk(self):
        print(f"Hi i am {self.name}")


john = Person("John Smith")
john.talk()