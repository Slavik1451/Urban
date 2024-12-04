class Human:

    head = 1 # атрибут класса, привязан к каждому элементу класса по умолчанию
    # def __init__ - конструктор класса
    # self - указатель на атрибут экземпляра класса
    def __init__(self, name, age=0): # функция  внутри класса - метод
        # У каждого объекта может быть своя характеристика - атрибут
        self.name = name  # У каждого объекта будет своё имя. Инициализируем атрибут
        self.age = age    # У каждого объекта будет свой возраст
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'Я {self.name}, у меня день рождения, мне теперь {self.age} лет')

    def __len__(self):
        return self.age

    def __lt__ (self, other): # этот метод вызывается, когда ты используешь оператор < для сравнения двух объектов.
        return self.age < other.age

    def __gt__(self, other): # этот метод вызывается, когда ты используешь оператор < для сравнения двух объектов.
        return self.age > other.age

    def __str__(self): # Этот метод вызывается, когда вызываются str() или print() для получения представления объекта.
        return f'{self.name}'



# Создаём объект (человека)
person1 = Human("Вячеслав", 24)
person2 = Human('Илья', 23)


print(person2)


# person1.say_info() # class - human, Тип данных - person. Метод - say_info
# person2.say_info()
# person1.birthday()
# print(len(person2))