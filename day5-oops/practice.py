# Create a class "Programmer" for storing information of few programmers working at microsoft 

class Programmer:
    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language

nipun = Programmer("Nipun",2400000,"python")
print(nipun.salary,nipun.language)