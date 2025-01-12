n=int(input('Введите число.'))

for i in range(1, int(n) + 1):
	print(i)
	

one=int(input('Введите первое число.'))
two=int(input('Введите второе число.'))
if one>two:
	print('Большое число:', one)
elif one<two:
	print('Большое число:', two)
else:
	print('Они равны.')