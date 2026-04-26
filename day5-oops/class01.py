class Employee:
    language = "Py"
    salary = 1200000

nipun = Employee()
nipun.name = "Nipun"
# here name is an instance attribute and language and salary are class attribute as they belong directly to the class 
print(nipun.language,nipun.salary,nipun.name)