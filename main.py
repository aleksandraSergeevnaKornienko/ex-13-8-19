ticket = int(input("Введите количество билетов "))
total = 0
for a in range(ticket):
    age = int(input("Введите возраст "))
    if age < 18:
        print("Стоимось билета 0 рублей")
    elif age < 25:
        print("Стоимость билета 990 рублей")
        total += 990
    else:
        print("Стоимость билета 1390 рублей")
        total += 1390


if ticket >= 3:
    print("Поздравляем скидка 10%")
    total *= 0.9
print("Итого к оплате ", int(total))

