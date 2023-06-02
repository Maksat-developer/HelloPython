# Приветствие
print("Добро пожаловать в мир программирования Python!")
print("Сейчас мы познакомимся с основными типами данных.")


# Строковый тип данных (string)
name = "Иван"
print("Имя:", name)
print("Методы для типа данных 'str':")
print("Длина строки:", len(name))
print("Преобразование в заглавные буквы:", name.upper())
print("Преобразование в строчные буквы:", name.lower())



# Целочисленный тип данных (integer)
age = 25
print("Возраст:", age)
print("Методы для типа данных 'int':")
print("Максимальное значение:", max(age))
print("Минимальное значение:", min(age))
print("Абсолютное значение:", abs(age))

# Вещественный тип данных (float)
weight = 62.5
print("Вес:", weight)
print("Методы для типа данных 'float':")
print("Округление до ближайшего целого числа:", round(weight))
print("Целая часть числа:", int(weight))
print("Десятичная часть числа:", weight % 1)


# Логический тип данных (boolean)
is_student = True
print("Студент:", is_student)
print("Методы для типа данных 'bool':")
print("Инвертирование значения:", not is_student)

# Список (list)
fruits = ["яблоко", "банан", "апельсин"]
print("Фрукты:", fruits)
print("Методы для типа данных 'list':")
print("Добавление элемента в конец списка:")
fruits.append("груша")
print(fruits)
print("Индекс элемента 'банан':", fruits.index("банан"))

# Кортеж (tuple)
coordinates = (3, 4)
print("Координаты:", coordinates)
print("Методы для типа данных 'tuple':")
print("Количество элементов в кортеже:", len(coordinates))
print("Сложение кортежей:", coordinates + (5, 6))

# Словарь (dictionary)
person = {
    "имя": "Анна",
    "возраст": 30,
    "профессия": "инженер"
}
print("Личная информация:", person)
print("Методы для типа данных 'dict':")
print("Ключи словаря:", person.keys())
print("Значения словаря:", person.values())

# Выводим информацию о типе данных
print("Тип переменной 'age':", type(age))
print("Тип переменной 'weight':", type(weight))
print("Тип переменной 'name':", type(name))
print("Тип переменной 'is_student':", type(is_student))
print("Тип переменной 'fruits':", type(fruits))
print("Тип переменной 'coordinates':", type(coordinates))
print("Тип переменной 'person':", type(person))

# Завершение программы
print("Спасибо за ознакомление! Удачи в изучении Python!")


