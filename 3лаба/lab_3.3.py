def read_file(filepath, method='all'):
    try:
        with open(filepath, 'r') as file:
            if method == 'all':
                content = file.read()
                print(content)
            elif method == 'line':
                for line in file:
                    print(line.strip())
            else:
                print("Неверный метод чтения.")
    except FileNotFoundError:
        print("Ошибка: Файл не найден. Пожалуйста, проверьте путь к файлу.")
read_file('./example.txt', 'line')