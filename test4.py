money = input('insert number of money: ')
amount_of_people = input('instre amoount of people : ')
product_value = int(money)/int(amount_of_people)
product_value_t = format(amount_of_people, ".2f")
print('you would get', product_value_t, "baht per peron")
print('you would get', product_value_t + "baht per peron")
print('you would get {} Bant per peron'.format (product_value_t))
print(f'you would get {product_value_t} Bant per pero')