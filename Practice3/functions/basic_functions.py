def greet():
    """Простая функция без аргументов."""
    print("Привет! Это базовая функция.")

def calculate_area(radius):
    """Функция с аргументом и возвращаемым значением."""
    return 3.14 * radius ** 2

greet()
print(f"Площадь круга: {calculate_area(5)}")