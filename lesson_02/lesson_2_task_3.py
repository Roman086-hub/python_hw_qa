import math


def square(n):
    return math.ceil(n ** 2)


s = float(input("Введите сторону квадрата:"))
results = square(s)

print(f"Площадь квадрата: {results}")
