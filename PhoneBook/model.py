phone_book=[]
start_phone_book=[]

PATH='HomeWork8\PYTHON_COURSES\PhoneBook\sample.txt'

def get_pb():
    global phone_book
    return phone_book

def load_file():
    global phone_book, start_phone_book
    with open(PATH,'r', encoding='UTF-8') as file:
        data=file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
    start_phone_book=phone_book.copy()

def save_contact():
    global phone_book
    data=[]
    for contact in phone_book:
        data.append(';'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)

def add_contact(contact:dict):
    global phone_book
    phone_book.append(contact)


def exit_pb()->bool:
    global phone_book, start_phone_book
    if phone_book==start_phone_book:
        return False
    else:
        return True
    
def find_contact(find_info: str)->list[dict]:
    with open(PATH,'r', encoding='UTF-8') as file:
        data=file.readlines()
    coincidence=0
    find_phone_book=[]
    for contact in data:
        if find_info in contact.lower():
            coincidence+=1
            contact = contact.strip().split(';')
            find_phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
    if coincidence==0:
        return None
    else:
        return find_phone_book
    

def change_contact(contact:list[dict], new_info:str, choice:int):
    global phone_book
    with open(PATH,'r', encoding='UTF-8') as file:    
        data=file.readlines()
    with open(PATH,'w', encoding='UTF-8') as file:
        old_contact=''
        for i in contact:
             old_contact=old_contact+';'.join(value for value in i.values())
        print(old_contact)
        old_contact_2=old_contact.split(';')
        print(old_contact_2)
        if choice==1:
            old_contact_2[0]=new_info
        if choice==2:
            old_contact_2[1]=new_info
        if choice==3:
            old_contact_2[2]=new_info
        str_list=';'.join(old_contact_2)
        print(str_list)
        for k in data:
            if old_contact in k:
                file.write(str_list+'\n')
            else:
                file.write(k)
        
   

def delete_contact(contact:list[dict], choice:bool):
    global phone_book
    with open(PATH,'r', encoding='UTF-8') as file:    
        data=file.readlines()
    with open(PATH,'w', encoding='UTF-8') as file:
        old_contact=''
        for i in contact:
            old_contact=old_contact+';'.join(value for value in i.values())
        for k in data:
            if old_contact not in k:
                file.write(k)

       
    