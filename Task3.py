from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)
attempt_count = 0
remains_attempts = 10

while attempt_count < 10:
    print('Введите число от', LOWER_LIMIT, 'до', UPPER_LIMIT)
    guess = int(input())
    attempt_count += 1
    remains_attempts -= 1
    if guess == secret_number:
        print('Поздравляем! Вы угадали число с', attempt_count, 'попытки!')
        break
    elif guess < secret_number:
        print('Загаданное число больше', guess)
        print('Осталось попыток:', remains_attempts)
    else:
        print('Загаданное число меньше', guess)
        print('Осталось попыток:', remains_attempts)

    if attempt_count >= 10:
        print('Вы использовали все 10 попыток. Загаданное число было:', secret_number)