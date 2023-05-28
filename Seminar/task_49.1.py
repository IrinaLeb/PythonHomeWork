# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - 
# данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# r - чтение файла 'read'
# w - перезаписывание файла 'write'
# a - добавление в файл 'append'

# with open('file.txt', 'w', encoding='utf-8') as file:
#     file.write('первая строка в этом файле')
    
# with open('file.txt', 'a', encoding='utf-8') as file:
#     file.write('\nвторая строка в этом файле')

# with open('file.txt', 'r', encoding='utf-8') as fd:
#     print(type(fd))
#     # z = fd.read()
#     z = fd.readlines()
#     for i in z:
#         print(i)
        
# Иван Иванов 12345
# Петр Иванов 77777

def add_contact(f):                           # добавление записи в тел.книгу
    input_name = input('Введите Имя: ')
    input_middle_name = input('Введите Отчество: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_last_name}; {input_name}; {input_middle_name}; - {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')


def read_all(f):                             # чтение всех записей в тел.книги
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list
        

def print_all(f):                            # вывод всех записей в тел.книги
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)
    

def search_contact(f):                        # поиск в тел.книги
    last_name = input('Введите ФИО или номер телефона для поиска: ')
    adr_book = read_all(f)
    print(len(adr_book))
    for i in range(len(adr_book)):
        print(i, adr_book[i])
    idx = int(input('Введите индекс для замены: '))
    last_name, name, _ = adr_book[idx].split('; ')
    phone = input('Новый номер: ')
    new_record = f'{last_name}; {name}; {phone}'
    adr_book[idx] = new_record
    with open(f, 'w', encoding='utf-8') as fd:
        fd.writelines(adr_book)
    # for line in adr_book:
    #     if last_name in line:
    #         line = line.replace(';', '')
    #         line = line.replace('\n', '')
    #         print (line)
    # else:
    #     print('Такой записи нет в телефонной книги')


def main():
    # user_choice = ''
    # while user_choice != 'z':
    file = 'adress_book.txt'
    while True:
        user_choice = input('1 - добавить запись \n2 - прочитать всю тел.книгу' 
                            '\n3 - найти запись \n0 - для выхода \nВыберите номер из меню: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == '0':
            print('Всего хорошего')
            break
            

if __name__ == '__main__':
    main()