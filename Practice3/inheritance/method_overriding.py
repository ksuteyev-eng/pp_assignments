class Bird:
    def sound(self):
        print("Птица поет")

class Crow(Bird):
    def sound(self):
        """Переопределение метода родителя."""
        print("Кар-кар!")

crow = Crow()
crow.sound()