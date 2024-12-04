class House:
    House_stryktyra = 'kirpich'
    standart_floor = 15

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
            print('Вы приехали')
        else:
            print('Такого этажа не существует')



h1 = House('Жк Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print(h2.House_stryktyra)
print(h1.House_stryktyra)
print(House.House_stryktyra)

h1.House_stryktyra = 'Дерево'
House.House_stryktyra = 'Бетон'

print(h2.House_stryktyra)
print(h1.House_stryktyra)
print(House.House_stryktyra)

