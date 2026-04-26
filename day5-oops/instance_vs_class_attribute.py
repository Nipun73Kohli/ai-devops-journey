class Employee:
    language = "Py"
    salary = 1200000
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    # if we don't want to pass an object as an argument in the method we can craete a static method 

    @staticmethod
    def greet():
        print("Hi")

nipun = Employee()
nipun.language = "JS"
nipun.getInfo() # This automatically gets converted into Employee.getInfo(nipun) if you wouldn't have 
#provided self as an argument in the method it will throw an error and zero arguments were present in the intialisation
nipun.greet()

