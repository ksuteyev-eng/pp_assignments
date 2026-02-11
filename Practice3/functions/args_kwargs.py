def print_everything(*args, **kwargs):
    """Демонстрация работы *args (кортеж) и **kwargs (словарь)."""
    print("Позиционные аргументы:", args)
    print("Именованные аргументы:", kwargs)

print_everything(1, 2, 3, status="active", role="admin")