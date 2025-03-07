class friend:
    School ="Onkur School"
    def __init__(self, name , age):
        self.name =name 
        self.age=age 

    def show(self):
        print(f"Name : {self.name}\nAge : {self.age}\nSchool : {self.School}")  
    
tanisha=friend('Tanisha', 13)
Safa =friend('Safa', 12)
soha =friend('Soha' ,14)

tanisha.show()
print("\n")
Safa.show()
print("\n")
soha.show()
       
       