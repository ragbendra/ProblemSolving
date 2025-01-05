class Person:  # class instantiate
    def __init__(self,n,o):  #  Constructor function. It will get executed automatically whenever an object is created
        print("This is constructor execution upon object creation.")
        self.name = n
        self.occ = o
    # name = "happy"
    # occ = "Data Scientist"
    def info(self):  # Method. Function defined inside a class is method.
        print(f"{self.name} is a {self.occ}")
a = Person("Saiju","Data Analyst")  # object creation
b = Person("Prajwal","Web Developer")   # object creation
a.info()  # method calling
b.info()  # method calling