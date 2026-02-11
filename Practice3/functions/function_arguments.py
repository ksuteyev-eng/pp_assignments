def describe_pet(name, animal_type="собака"):
    """Функция с позиционным и дефолтным аргументами."""
    print(f"У меня есть {animal_type} по имени {name}.")

describe_pet("Вилли")
describe_pet("Мурка", "кошка")