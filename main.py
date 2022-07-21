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



# numbers = [5, 6, 7, 2, 8, 2,7]
# even_list = [number % 2 == 0 for number in numbers]
# answer = not all(even_list) and any(even_list)
# print(answer)

# M = [[i * j for j in range(1,11)] for i in range(1,11)]
# print(M)




# a = False
# b = False
# if a and b :
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b :
#     print("Одна из переменных истинная")
#     print(a or b) # печать значения одной
# else:
#     print(a,b, "Обе переменные не истены")
