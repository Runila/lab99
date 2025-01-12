from  mod  import MyModule
from  mod  import modul2

x=int(input('Введите первое число:'))
y=int(input('Введите второе число:'))
ones=input('Введите текст: ')

two=MyModule.sum(x,y)
two2=MyModule.multiply(x,y)
one=modul2.reverse_string(ones)

print(one)
print(two)
print(two2)