class Phone:
    def __init__(self, brand):
        self.brand = brand

class SmartPhone(Phone):
    def __init__(self, brand, os):
        # super() вызывает конструктор родителя
        super().__init__(brand)
        self.os = os

iphone = SmartPhone("Apple", "iOS")
print(f"Бренд: {iphone.brand}, ОС: {iphone.os}")