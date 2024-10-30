import json
number = imput("введите номер квалификации: ")
numbers = number[:len{number} - 3]
found = True
with open("dump.json", 'r') as file:
    data = json.load(file)
    for item in data:
        if item['model'] == "data.spec" and item['files']['code'] == numbers:
            print(f"=============== Найдено ===============")
            print(f"{item['code']} >> Специальность "{item['titel']}", ПТО")
            print(f"{item['fields']} >> Квалификация "{item['code']}"")
        if item['model'] == "data.spec" and item['files']['code'] == number:
            print(f"=============== Не найдено ===============")
if found:

