x = 0
while x == 0:
    user_input = str(input('Введите текст: '))
    file = open('./3лаба/user_input.txt', 'a', encoding='utf-8')
    file.write(user_input)
    file = open('./3лаба/user_input.txt', encoding='utf-8')
    print(file.read())
    break_point = str(input("Хотите ли вы остановить программу? (да/д)"))
    if break_point.lower() == "да" or break_point.lower() == "д":
        file.close()
        break
