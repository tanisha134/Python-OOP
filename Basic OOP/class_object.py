class hira:
    def __init__(self, name , age):
        self.name =name 
        self.age=age
    
    def show(self):
        return f"My name is {self.name} and my age is {self.age}"

    
object1=hira("Hira", 26)
print(object1.show())

        