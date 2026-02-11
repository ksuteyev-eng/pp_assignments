class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        """Метод экземпляра с использованием self."""
        print(f"Привет, я робот {self.name}!")

bot = Robot("R2D2")
bot.say_hello()