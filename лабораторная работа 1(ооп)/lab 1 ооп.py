# TODO Написать 3 класса с документацией и аннотацией типов

class Phone:
    def __init__(self, color: str, count_screen, serial_number: str):
        if not isinstance(color, str):
            raise TypeError('Должен быть назван цвет')
        self.color = color
        if count_screen >= 2:
            raise TypeError('телефон бывает только с одним экраном')
        self.count_screen = count_screen
        if not isinstance(serial_number, str):
            raise TypeError('модель телефона содержит название и число')
        self.serial_number = serial_number

class Book:
    def __init__(self, author: str, pages, weight: int):
        if not isinstance(author, str):
            raise TypeError('у книги должен быть автор')
        self.author = author
        if pages <= 10:
            raise ValueError('книга должна иметь больше 10 страниц')
        self.pages = pages
        if weight > 10000:
            raise ValueError('книга имеет меньший вес')
        self.weight = weight

class Flats:
    def __init__(self, floor_number: int, entrance: int):
        if not isinstance(floor_number, int):
            raise TypeError('этаж квартиры должен быть записан цифрой')
        if floor_number <= 0:
            raise ValueError('квартира не может находиться ниже нулевого уровня')
        self.floor_number = floor_number
        if entrance <= 0:
            raise ValueError('квартира должна иметь вход')
        self.entrance = entrance

if __name__ == "__main__":
    iphone_14 = Phone('фиолетовый', 1, 'айфон 14')
    the_catcher_in_the_rye = Book('salinger', 234, 1)
    flat = Flats(5, 2)
    import doctest
    doctest.testmod()
    pass