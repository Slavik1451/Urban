class Human:
    # def __init__ - конструктор класса
    # self - указатель на экземпляр класса
    def __init__(self, name, age = 0): # функция  внутри класса - метод
        # У каждого объекта может быть своя характеристика - атрибут
        self.name = name  # У каждого объекта будет своё имя. Инициализируем атрибут
        self.age = age    # У каждого объекта будет свой возраст
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'Я {self.name}, у меня день рождения, мне теперь {self.age} лет')

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age


# Создаём объект (человека)
person = Human("Вячеслав", 24)
print(person.name)  # Выведет: Вячеслав
print(person.age)   # Выведет: 30
person2 = Human("Антон")

person2.change_name('Марина')
person2.change_age(25)

person.say_info() # class - human, Тип данных - person. Метод - say_info
person2.say_info()

person.birthday()




