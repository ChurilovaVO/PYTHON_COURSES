def main_menu():
    menu=['1. Посмотреть контакты','2. Создать контакт','3. Найти контакт',
                          '4. Изменить контакт','5. Удалить контакт','6. Выход']
    for i in menu:
        print(i)
    
def show_contact():
    file=open('HomeWork8\PYTHON_COURSES\HomeWork8\sample.txt', 'r', encoding='UTF-8')
    data=file.readlines()
    for i in data:
        print(i)
    file.close
      
def add_contact():
    file=open('HomeWork8\PYTHON_COURSES\HomeWork8\sample.txt', 'a', encoding='UTF-8')
    data=file.write(input('Введите имя, телефон и комментарий (разделяя ;): '))
    file.write('\n')
    file.close
    print(f'Контакт добавлен в справочник')
        
def find_contact():
    find_info=input('Введите данные для поиска: ')
    file=open('HomeWork8\PYTHON_COURSES\HomeWork8\sample.txt', 'r', encoding='UTF-8')
    data=file.readlines()
    coincidence=0
    for i in data:
        if find_info in i.lower():
            print(i)
            coincidence+=1
    if coincidence==0:
        print('Не найдено')
    file.close
       
def change_contact():
    file=open('HomeWork8\PYTHON_COURSES\HomeWork8\sample.txt', 'r', encoding='UTF-8')
    data=file.readlines()
    copy_data=data.copy()
    find_info=input('Какой контакт изменить?: ')
    for change_string in data:
        if find_info in change_string.lower():
            found_contact=change_string
            print(found_contact)
    list=found_contact.split(';')
    file.close
    file=open('HomeWork8\PYTHON_COURSES\HomeWork8\sample.txt', 'w', encoding='UTF-8')
    change_menu=['Что изменить?','1.Фио', '2.Телефон', '3.Комментарий']
    for j in change_menu:
        print(j)
    change_info=int(input('Введите соответствующую цифру: '))
    if change_info==1:
        new_name=input('Напишите имя контакта: ')
        list[0]=new_name
        print(f'Имя контакта изменено на: {new_name}')
    if change_info==2:
        new_tel=input('Напишите телефон контакта: ')
        list[1]=new_tel
        print(f'Телефон контакта изменен на: {new_tel}')
    if change_info==3:
        new_com=input('Напишите комментарий к контакту: ')
        list[2]=new_com
        print(f'Комментарий контакта изменен на: {new_com}')
    str_list=';'.join(list)
    for k in copy_data:
        if found_contact in k:
            file.write(str_list)
        else:
            file.write(k)
    file.close
            
def delete_contact():
    file=open('HomeWork8\PYTHON_COURSES\HomeWork8\sample.txt', 'r', encoding='UTF-8')
    data=file.readlines()
    copy_data=data.copy()
    delete_info=input('Какой контакт удалить?: ')
    for change_string in data:
        if delete_info in change_string.lower():
            found_contact=change_string
    file=open('HomeWork8\PYTHON_COURSES\HomeWork8\sample.txt', 'w', encoding='UTF-8')
    delete_info2=input(f'Удалить контакт: {found_contact} ?(да/нет): ')
    if delete_info2=='да':
        for k in copy_data:
            if found_contact not in k:
                file.write(k)
        print(f'Контакт:{found_contact} удален')
    file.close
        
main_menu()
choice=None
while choice!=6:
    choice=int(input('Выберите пункт действия: '))
    if choice==1:
        show_contact()
    if choice==2:
        add_contact()
    if choice==3:
        find_contact() 
    if choice==4:
        change_contact()
    if choice==5:
        delete_contact()
    if choice==6:
        print("Пока пока!")
        break
    choice_main_menu=input('Вернуться в главное меню? (да/нет): ')
    if choice_main_menu=='да':
        main_menu()
    
