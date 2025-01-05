class cars:
    def __init__(self,Ownername,Carbrand):
        self.name=Ownername  # self parameter is the reference to the current instance of the class, and is used to access the variable that belongs to the class.
        self.brand=Carbrand
    def info(self):
        print(f"{self.name} bought a new {self.brand}.")
s1=cars("Raghabendra","Mercedes")
print(s1.name)
s1.info()