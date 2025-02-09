import os 

bd_file = "database.txt"

def read_bd(): #чтение йоу 
    if not os.path.exists(bd_file):
        return []
    with open(bd_file, "r") as f:
        return [line.strip() for line in f.readlines()]

def write_bd(data): #пишем йоу
    with open(bd_file, "w") as f:
        f.writelines("\n".join(data))

def list_records():
    records = read_bd()
    if not records:
        print("БД пустая")
    else:
        for i, record in enumerate(records, 1):
            print(f"{i}. {record}")

def add_record():
    record = input("Введите запись: ")
    records = read_bd()
    records.append(record)
    write_bd(records)
    print("Добавили!")

def delete_record():
    list_records()
    try:
        index = int(input("Запись какого номера хотите удалить? \n")) -1
        records = read_bd()
        if 0 <= index < len(records):
            records.pop(index)
            write_bd(records)
            print("Запись была удалена.")
        else: 
            print("Такого нет :(")
    except ValueError:
        print("Число надо!")

def edit_record():
    list_records()
    try:
        index = int(input("Запись какого номера вы хотите отредактировать? \n")) -1
        records = read_bd()
        if 0 <= index < len(records):
            new_rec= input("Введитье новое значение: \n")
            records [index] = new_rec
            write_bd(records)
            print("Успешено")
        else:
            print("Такого нет :(")
    except ValueError:
        print("Число надо!")
def main():
    while True:
        print("\nКоманды: \n 1. Прочитать \n 2. Добавить запись \n 3. Удалить запись \n 4. Редактировать запись")
        print("\n 5. Завершить работу. \n")
        command  = int(input("Введите номре команды: "))
        if command == 1:
            list_records()
        elif command == 2:
            add_record()
        elif command == 3:
            delete_record()
        elif command == 4:
            edit_record()
        elif command == 5:
            break
        else:
            print("У нас такого нет :( ")
if __name__ == "__main__":
    main()