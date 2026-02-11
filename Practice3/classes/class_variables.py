class Employee:
    company = "TechCorp"  # Переменная класса

    def __init__(self, name):
        self.name = name  # Переменная экземпляра

emp1 = Employee("Alice")
print(f"{emp1.name} работает в {Employee.company}")