class Employee:
    language = "Py"
    salary = 1200000
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    def __init__(self,name,salary,language):    # This is called a dunder method as it starts with __ and it is automatically called when an object is created 
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

# if we don't want to pass an object as an argument in the method we can craete a static method 

    @staticmethod
    def greet():
        print("Hi")

nipun = Employee("Nipun",1300000,"JS")
print(nipun.salary,nipun.language)