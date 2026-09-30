def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


n = int(input("Введите год: "))
result = is_year_leap(n)

print(f"год {n}: {result}")
