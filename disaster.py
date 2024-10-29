# disaster.py
# Козлов Иван
# Класс для работы с объектом "Стихийное бедствие"
# Этот класс включает закрытые поля, декоратор и метод приведения к строке.


def casualties_to_readable(getter_func):
    def wrapper(instance): #вызов экземпляра класса
        casualties = getter_func(instance)

        def format_number(num):
            units = ['человек', 'тысяча', 'тыс.', 'миллион', 'млн.']
            suffixes = ['', '', 'та', '', 'а']

            if num >= 1_000_000:
                return f"{num / 1_000_000:.1f} млн."
            elif num >= 1_000:
                return f"{num / 1000:.1f} тыс."
            elif num > 100 < 500:
                return f"{num / 100} сотни"
            elif num >=500:
                return  f"{num / 100} сотен"
            elif num == 100:
                return f"{num//100} сотня"
            else:
                return f"{num} {units[num]}{suffixes[num // 10]}"

        return format_number(casualties)

    return wrapper
# Когда декоратор @casualties_to_readable применяется к методу класса, он создает новую функцию wrapper.
# Эта функция wrapper принимает один аргумент - экземпляр класса (instance).
# Внутри wrapper вызывается оригинальный метод класса через getter_func(instance).
# Результат этого вызова сохраняется в переменную casualties.
# Затем casualties передается в функцию format_number, которая форматирует его.


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