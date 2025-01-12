def greet(names):
    print("Hello " + names)
def square(one):
    m=int(one)**2
    print(m)
def  max_of_two(x,y):
    if x>y:
        print(x)
    elif x<y:
        print(y)
    elif x==y:
        print('Они равны.')

 
names = input("Введите ваше имя: ")
one=input('Число для квадрата: ')  
x=int(input('Первое число:'))
y=int(input('Второе число:'))


greet(names)
square(one)
max_of_two(x,y)