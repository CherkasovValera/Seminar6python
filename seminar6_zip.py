# Создание модуля чтения списка словарей из файла, при работе с телефонным справочником
def get_data ():

    dicts_from_file = []
    name_symbol=["id","secondname", "name", "lastname", "comment"]
    with open("bd.txt", "r",encoding="utf-8") as bd:
        
        for line in bd:
            dicts_from_file.append(dict(zip(name_symbol, line.split("::"))))

    return dicts_from_file

print(get_data ())