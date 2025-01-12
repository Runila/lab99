import math
import datetime


def sqrt(number):
    if number < 0:
        print("Нельзя извлечь корень из отрицательного числа.")
    else:
        print("Квадратный корень из вашего числа равен: " + str(math.sqrt(number)))
def date(agr):
    if agr=='Да' or agr=='да':
        print(str(datetime.datetime.now()))
    elif agr=='Нет' or agr=='нет':
        print("Как скажите.")
    else:
        print("Напишите: ДА или Нет")
    

    

agr = input("Хотите  узнать дату время  ?(Да/нет)").lower()
number = int(input("Введите число: "))
sqrt(number)
date(agr)