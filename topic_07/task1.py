# INIT
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("KAtya", 15)
print(person1.name)  
print(person1.age)   

# STR
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book1 = Book("A court of thrones and roses", "Saraj J Maas")
print(str(book1))  

# AADD
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)
num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(3, 4)
result = num1 + num2
print(f"Результат додавання: {result.real} + {result.imag}")  

# OBJECT
class CallableObject:
    def __call__(self, x):
        return x * x

callable_obj = CallableObject()
result = callable_obj(8)  
print(result) 



