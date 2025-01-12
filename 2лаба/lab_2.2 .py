def describe_person(name, age=30):
    print(f"Привет, {name.title()}. Тебе {age} лет?")


name = input("Введите ваше имя: ")
ages=input('Введите ваш возраст: ')
describe_person(name,30)