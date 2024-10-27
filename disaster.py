# disaster.py
# Козлов Иван
# Класс для работы с объектом "Стихийное бедствие"
# Этот класс включает закрытые поля, декоратор и метод приведения к строке.

def casualties_to_readable(getter_func):
    """Декоратор для форматирования числа погибших в понятный вид."""
    def wrapper(instance):
        casualties = getter_func(instance)
        if casualties >= 1_000_000:
            return f"{casualties // 1_000_000} миллионов"
        elif casualties >= 1_000:
            return f"{casualties // 1_000} тысяч"
        elif casualties >= 100:
            return f"{casualties // 100} сотен"
        else:
            return f"{casualties} человек"
    return wrapper

class NaturalDisaster:

    def __init__(self, disaster_type, location, casualties):
        """Инициализация класса 'Стихийное бедствие' с типом, местом и числом погибших."""
        self.__disaster_type = disaster_type
        self.__location = location
        self.__casualties = casualties

    @property
    def disaster_type(self):
        """Геттер для типа бедствия."""
        return self.__disaster_type

    @property
    def location(self):
        """Геттер для места бедствия."""
        return self.__location

    @property
    @casualties_to_readable
    def casualties(self):
        """Геттер для числа погибших с применением декоратора для форматирования."""
        return self.__casualties
    def __str__(self):
        """Метод для представления объекта в виде строки."""
        return f"Тип: {self.__disaster_type}, Место: {self.__location}, Число погибших: {self.casualties}"