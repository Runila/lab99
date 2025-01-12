def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return print(False)  
    return print(True)


n=int(input('Введите число: '))
is_prime(n)