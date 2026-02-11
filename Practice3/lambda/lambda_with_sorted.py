data = [("apple", 50), ("banana", 20), ("cherry", 80)]
# Сортировка списка кортежей по числу (второй элемент)
sorted_data = sorted(data, key=lambda x: x[1])
print(f"Отсортировано по цене: {sorted_data}")
