class CustomClass:
    def __init__(self):
        self.data = "This is a custom class."

    def display(self):
        print(f"The data of {self.__class__.__name__} is: {self.data}")

if __name__ == "__main__":
    example_instance = CustomClass()
    example_instance.display()  # Output: The data of CustomClass is: This is a custom class.
