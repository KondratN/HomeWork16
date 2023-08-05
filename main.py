class Animal:

    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def set_name(self):
        name = input("Введите имя животного: ")
        if name == '':
            self.__name = 'Без имени'
        else:
            self.__name = name

    def get_name(self):
        return self.__name

    def set_color(self):
        color = input("Введите цвет животного: ")
        if color == '':
            self.__color = 'Без цвета'
        else:
            self.__color = color

    def get_color(self):
        return self.__color

    def __str__(self):
        return f'Имя: {self.__name}, цвет: {self.__color}'


class Cat(Animal):

    def __init__(self, name, color):
        super().__init__(name, color)

    def set_name(self):
        super().set_name()

    def get_name(self):
        return super().get_name()

    def set_color(self):
        super().set_color()

    def get_color(self):
        return super().get_color()

    def welcome_voice(self):
        print('Мяу')

    def __str__(self):
        return f'Кот {super().__str__()}'

class Dog(Animal):

    def __init__(self, name, color):
        super().__init__(name, color)

    def set_name(self):
        super().set_name()

    def get_name(self):
        return super().get_name()

    def set_color(self):
        super().set_color()

    def get_color(self):
        return super().get_color()

    def welcome_voice(self):
        print('Гав')

    def __str__(self):
        return f'Собака {super().__str__()}'


cat1 = Cat('Мурзик', 'Белый')
dog1 = Dog('Бобик', 'Красный')
print(dog1)
print(cat1)