number_ticket = int(input('Введите количество билетов: '))
sum = 0
for i in range(number_ticket):
    age = int(input('Введите возраст: '))
    if age < 18:
        sum += 0
    elif 18 <= age < 25:
        sum += 990
    elif age >= 25:
        sum += 1390
#При покупке больше трех билетов на конференцию,
# предоставляется скидка 10% от стоимости заказа
if number_ticket > 3:
    sum = sum * 0.9
print("Сумма к оплате:", int(sum), "рублей")
