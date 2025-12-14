# чтение файла
# file = open('text.txt', 'r', encoding='utf-8')
# try:
#     text = file.read()
#     print(text)
# except Exception as e:
#     print(e)
# finally:
#     file.close()

# Попробуйте открыть файлы с разными значениями mode для чтения.
file = open('text2.txt', 'a+', encoding='utf-8')
try:
    file.seek(0)
    text = file.read()
    print(text)

except Exception as e:
    print(e)
finally:
    file.close()

print('------------------')

# актуальный вариант
with open('end.txt', 'w+', encoding='utf-8') as file:
    file.write('Какой-то текст')
    file.seek(0)
    print(file.read())