
from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt
def get_info():
    is_valid_first_name = False
    is_valid_last_name = False
    while not is_valid_first_name or not is_valid_last_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise NameError("Не валидная фамилия")
            
            else:
                is_valid_first_name = True
                is_valid_last_name = True
        except NameError as err:
            print(err)
            continue
    
    
    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


def create_file(file_name):    
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телефон уже есть")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def replace_file(file_name, sourse_file_name, num):
    res = read_file(sourse_file_name)       
    for el in res:
        if el["Телефон"] == str(num):                       
            el = [el["Имя"], el["Фамилия"], el["Телефон"]]
            write_file(file_name, el) 

def delete_file(file_name, num):
    res = read_file(file_name)
    with open(file_name, "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        obj = []
        for el in res:
            if el["Телефон"] != str(num):
                obj.append(el)
        f_writer.writerows(obj)


def change_file(file_name, num):
    res = read_file(file_name)
    with open(file_name, "w", encoding="utf-8", newline="") as data:
        f_writer = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        obj = []
        for el in res:
            if el["Телефон"] == str(num):
                is_valid_first_name = False                
                is_valid_last_name = False
                while not is_valid_first_name or not is_valid_last_name:
                    try:
                        first_name = input("Введите имя: ")
                        if len(first_name) < 2:
                            raise NameError("Не валидное имя")
                        last_name = input("Введите фамилию: ")
                        if len(last_name) < 2:
                            raise NameError("Не валидная фамилия")                        
                        else:
                            is_valid_first_name = True
                            is_valid_last_name = True
                    except NameError as err:
                        print(err)
                        continue
                
                el["Имя"] = first_name
                el["Фамилия"] = last_name                
            obj.append(el)
        f_writer.writerows(obj)


def main():
    while True:
        command = input("Добро пожаловать в справочник!\n q - выход\n w - записать\n r - прочитать\n d - удалить\n e - изменить\n n - записать новый контакт из другого файла:\n Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':            
            print(*read_file(file_name))
        elif command == 'd':
            del_command = input("Введите телефон адресата, данные которого надо удалить: ")      
            delete_file(file_name, del_command)
        elif command == "e":  
            num = input("Введите телефон адресата, данные которого надо изменить: ")            
            change_file(file_name, num)
        elif command == "n":  
            num = input("Введите телефон адресата, данные которого перенесем из справочника NEW?: ")
            replace_file(file_name, sourse_file_name, num)

sourse_file_name = "new.csv"
file_name = "phone.csv"

main()