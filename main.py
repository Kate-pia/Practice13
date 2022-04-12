number_ticket = int(input('Введите количество билетов: '))
sum = 0
for i in range(number_ticket):
    age = int(input('Введите возраст: '))
    if age < 18:
        price = 0
        sum += price
    if 18 <= age < 25:
        price1 = 990
        sum += price1
    if age >= 25:
        price2 = 1390
        sum += price2
#При покупке больше трех билетов на конференцию,
# предоставляется скидка 10% от стоимости заказа
if number_ticket > 3:
    sum = sum * 0.9
print("Сумма к оплате:", int(sum), "рублей")