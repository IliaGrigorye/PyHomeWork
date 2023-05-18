num = int(input("Введите число: "))
if num <= 0 or num > 100000:
    print("Некорректный ввод числа")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
        break
    if is_prime:
        print("Число", num, "является простым")
    else:
        print("Число", num, "является составным")