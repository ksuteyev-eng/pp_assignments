prices = [100, 500, 250, 800, 150]
# Фильтрация: оставляем цены выше 300
expensive = list(filter(lambda p: p > 300, prices))
print(f"Дорогие товары: {expensive}")