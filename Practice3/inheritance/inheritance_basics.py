class Parent:
    def greet(self):
        print("Привет от родителя")

class Child(Parent):
    """Дочерний класс наследует методы родителя."""
    pass

c = Child()
c.greet()