new_list = [3, 5, 7, 9, 10.5]
print(new_list)

new_list.append("Python")
print(f"Новый список: {new_list}\nЕго длина: {len(new_list)}")
print(f"Первый элемент:{new_list[0]}\nПоследний элемент: {new_list[-1]}\nСо второго по четвёртый:{new_list[1:4]}")
new_list.remove("Python")
print(f"Мы удалили Пайтон, список выглядит так: {new_list}\nего длина: {len(new_list)}")

print("-"*30)
new_list = [3, 5, 7, 9, 10.5]
list_reversed = new_list[-1::-1]
print(list_reversed)

