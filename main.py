import json #подключение модуля
number = input("введите номер квалификации: ")
numbers = number [:len(number) - 3] #ввод номера
found = True #счетчик
with open('dump.json', 'r', encoding='utf-8') as file: #открывает файл
    data = json.load(file)
    for item in data: #просматривает файл и записывает 
        if item['model'] == "data.specialty" and item["fields"]["code"] == numbers:
            print("=============== Найдено ===============")
            print(f'{numbers} >> Специальность "{item["fields"]["title"]}", {item["fields"]["c_type"]}')
            found = False
        if item['model'] == "data.skill" and item["fields"]["code"] == number:
            print(f'{number} >> Специальность "{item["fields"]["title"]}"')
if found: #выводится если не найдено
    print ("=============== Не найдено ===============")
