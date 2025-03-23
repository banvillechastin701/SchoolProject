class MyClass:
    def __init__(self):
        self.my_variable = 10

    def another_method(self):
        print("Another method")

class ComplexObject:
    def __init__(self):
        self.__my_variable = 20

obj = MyClass()
ComplexObject()

# Test the class MyClass
print(obj.my_variable)

# Test the class ComplexObject
print(ComplexObject().__my_variable)
