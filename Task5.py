from fractions import Fraction

def add_fractions(frac1, frac2):
    result = frac1 + frac2
    return result

def multiply_fractions(frac1, frac2):
    result = frac1 * frac2
    return result

frac1 = Fraction(input("Введите первую дробь: "))
frac2 = Fraction(input("Введите вторую дробь: "))

print("Сумма дробей:", add_fractions(frac1, frac2))
print("Произведение дробей:", multiply_fractions(frac1, frac2))