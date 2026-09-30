def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    else:
        return n


num = int(input("Введите число: "))
for i in range(1, num + 1):
    print(fizz_buzz(i))


