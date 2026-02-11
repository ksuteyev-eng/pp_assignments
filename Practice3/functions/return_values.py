def get_user_data(first, last):
    """Возвращает словарь как результат работы функции."""
    return {"first_name": first, "last_name": last}

def show_list(items):
    """Пример передачи списка в качестве аргумента."""
    for item in items:
        print(f"Элемент: {item}")

user = get_user_data("Иван", "Петров")
print(user)
show_list(["Python", "Java", "C++"])