# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.


def custom_write(file_name: str, strings: list[str]) -> dict:

    stringsInfo: dict = {}

    with open(file=file_name, mode='w', encoding='UTF-8') as file:

        stringNumber: int = 0

        for string in strings:

            stringNumber += 1

            stringsInfo[(stringNumber, file.tell())] = string
            file.write(string + '\n')

    return stringsInfo


print(custom_write('example.txt', ['string1', 'string2']))
