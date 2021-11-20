def format_price(price):
    price = int(price)
    string_result = f"Цена: {price} руб."
    return string_result

my_price = 56.24

string_result = format_price(my_price)
print(string_result)

