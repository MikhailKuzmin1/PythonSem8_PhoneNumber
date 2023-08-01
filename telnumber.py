# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

import os

filename = 'tell.txt'

def load_tel():
    if os.path.isfile(filename):
        with open(filename, encoding='utf-8') as f:
            r = f.readlines()
            s = []
            for line in r:
                s.append(line.split())
        return s
    s = []
    return s

def input_tel(s):
    first_name = input('Введите имя: ')
    patronimic = input('Введите отчество: ')
    last_name = input('Введите фамилию: ')
    tel = input('Введите номер телефона: ')
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{last_name} {first_name} {patronimic} {tel} \n')
    s.append([last_name, first_name, patronimic, tel])
    return s

def search_tel(s, object):
    for line in s:
        if object in line or object.capitalize() in line:
            print(" ".join(line))
    
def show_tel(s):
    for line in s:
        print(" ".join(line))

def delete_tel(s, object):
    for line in s:
        if object in line:
            s.remove(line)
    with open(filename, 'w', encoding='utf-8') as f:
        for line in s:
            f.write(f'{" ".join(line)}\n')
    return s

def replace_tel(s, object):
    print(f'Выбран {" ".join(s[object - 1])}')
    replaice_choice = input('Что хотите изменить?\n1 - Фамилия\n2 - Имя\n3 - Отчество\n4 - Номер телефона\n')
    match replaice_choice:
        case'1':
            new_lastname = input('Введите новую фамилию: ')
            index = 0
            s[object-1][index] = new_lastname
        case'2':
            new_name = input('Введите новое имя: ')
            index = 1
            s[object-1][index] = new_name
        case'3':
            new_patronimic = input('Введите новое отчество: ')
            index = 2
            s[object-1][index] = new_patronimic
        case'4':
            new_phone = input('Введите новый номер: ')
            index = 3
            s[object-1][index] = new_phone
        case _:
            print('Некоректный ввод')
    with open(filename, 'w', encoding='utf-8') as f:
        for line in s:
            f.write(f'{" ".join(line)}\n')
    return s    

if __name__ == '__main__':
    s = load_tel()
    while True:
        print('Меню')
        action = input('1 - Добавить данные \n2 - Поиск \n3 - показать справочник \n4 - Удалить запись \n5 - Изменить запись  \n6 - Выход \n')
        match action:
            case'1':
                s = input_tel(s)
            case'2':
                search_name = input('Введите имя или фамилию для поиска: ')
                search_tel(s, search_name)
            case'3':
                show_tel(s)
            case'4':
                delete_name = input('Введите имя или фамилию для удаления: ')
                delete_tel(s, delete_name)
            case'5':
                number = 1
                for line in s:
                    print(f'{number} -  {" ".join(line)}')
                    number += 1
                replace_name = int(input('Введите номер человека, чьи данные необходимо изменить?: '))
                replace_tel(s, replace_name)
            case'6':
                break
            case _:
                print('Некоректный ввод')
