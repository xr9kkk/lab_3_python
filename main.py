# main.py
# Козлов Иван
# Программа для работы с классом "Стихийное бедствие"
# Программа выводит меню и позволяет пользователю выполнить различные действия с объектами класса NaturalDisaster.

from disaster import NaturalDisaster

N, M = 10, 5  # Константы, задаваемые в начале кода

def main():
    disasters = []
    while True:
        print("\nМеню:")
        print("1. Добавить новое бедствие")
        print("2. Просмотреть все бедствия")
        print("3. Сохранить в файл")
        print("4. Загрузить из файла")
        print("5. Завершить программу")

        choice = input("Выберите действие (1-5): ")
        if choice == "1":
            add_disaster(disasters)
        elif choice == "2":
            view_disasters(disasters)
        elif choice == "3":
            save_to_file(disasters)
        elif choice == "4":
            load_from_file(disasters)
        elif choice == "5":
            print("Завершение программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

def add_disaster(disasters):
    """Функция для добавления нового стихийного бедствия."""
    disaster_type = input("Введите тип бедствия: ")
    location = input("Введите место бедствия: ")
    try:
        casualties = int(input("Введите число погибших: "))
    except ValueError:
        print("Число погибших должно быть числом.")
        return
    disaster = NaturalDisaster(disaster_type, location, casualties)
    disasters.append(disaster)
    print("Бедствие добавлено.")

def view_disasters(disasters):
    """Функция для отображения всех бедствий."""
    if not disasters:
        print("Список бедствий пуст.")
    for i, disaster in enumerate(disasters, start=1):
        print(f"{i}. {disaster}")

def save_to_file(disasters):
    """Сохранение бедствий в файл."""
    filename = input("Введите имя файла для сохранения: ")
    try:
        with open(filename, "w", encoding="utf-16") as file:
            for disaster in disasters:
                file.write(f"{disaster.disaster_type},{disaster.location},{disaster._NaturalDisaster__casualties}\n")
        print("Данные сохранены.")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def load_from_file(disasters):
    """Загрузка бедствий из файла."""
    filename = input("Введите имя файла для загрузки: ")
    try:
        with open(filename, "r", encoding="utf-16") as file:
            for line in file:
                disaster_type, location, casualties = line.strip().split(',')
                disaster = NaturalDisaster(disaster_type, location, int(casualties))
                disasters.append(disaster)
        print("Данные загружены.")
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")


if __name__ == "__main__":
    main()