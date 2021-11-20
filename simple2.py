def user_number():
    number_input = input("Введите число от 1 до 10: ")
    try:
        number_input_formatted = number_input.strip()
        final_number = int(number_input)+10
        return final_number
    except:
        print("Мы не смогли распознать ваше число!")

print(f"Число на 10 больше: {user_number()}")