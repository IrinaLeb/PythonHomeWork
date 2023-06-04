# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# r - чтение файла 'read'
# w - перезаписывание файла 'write'
# a - добавление в файл 'append'


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
        line = line.replace('\n', '')
        line = line.replace(';', '')
        print(line)
    

def search_contact(f):                        # поиск в тел.книги
    search_line = input('Введите ФИО или номер телефона для поиска: ')
    adr_book = read_all(f)
    for line in adr_book:
        if search_line in line:
            line = line.replace(';', '')
            line = line.replace('\n', '')
            print (line)        
            
               
def change_contact(f):
    change_name = input('Введите ФИО или номер телефона для поиска: ')
    adr_book = read_all(f)
    for i in range(len(adr_book)):
        for line in adr_book:
            if change_name in line:
                line = line.replace(';', '')
                line = line.replace('\n', '')
            #print (line)        
    # print(adr_book)
    
        print(line[i])
        
    idx = int(input('Введите индекс для замены: '))
    last_name, name, _ = adr_book[idx].split('; ')
    phone = input('Новый номер: ')
    new_record = f'{last_name}; {name}; {phone}'
    adr_book[idx] = new_record
    with open(f, 'w', encoding='utf-8') as fd:
        fd.writelines(adr_book)
   
  


def main():
    # user_choice = ''
    # while user_choice != 'z':
    file = 'adress_book.txt'
    while True:
        user_choice = input('1 - добавить запись \n2 - прочитать всю тел.книгу \n3 - найти запись' 
                            '\n4 - изменения в тел.книги \n0 - для выхода \nВыберите номер из меню: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == '4':
            change_contact(file)        
        elif user_choice == '0':
            print('Всего хорошего')
            break
            

if __name__ == '__main__':
    main()