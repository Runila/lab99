with open('./3лаба/example.txt', encoding='utf-8') as file:
    print(file.read(7))
    file.seek(0)
    z = len(file.readline())
    print(file.readline(z))
    file.seek(0)
    print(file.read())
    file.close()


