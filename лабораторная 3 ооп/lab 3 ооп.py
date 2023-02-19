class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages
    if isinstance(pages, int):
        if pages > 0:
            self.pages = pages
        else:
            raise ValueError(f"Неверный номер страницы: {pages!r}")
    else:
        raise ValueError("Номер страницы должен быть в цифровом формате")

    def __str__(self):
        super_str = super().__str__()
        return f"Количество страниц: {self.pages}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f"{self.__class__.__name__}(pages = {self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    if isinstance(duration, float):
        if duration > 0:
            self.duration = duration
        else:
            raise ValueError(f"Задана неверная длительность: {duration!r}")
    else:
        raise ValueError("Должна быть задана длительность")

    def __str__(self):
       aud_str = super().__str__()
       return f"Продолжительность {self.duration!r}"

    def __repr__(self):
        aud_repr = super().__repr__()
        return f"{self.__class__.__name__}(duration = {self.duration!r}"


if __name__ == "__main__":
    book1 = PaperBook("Ночь в Лиссабоне", "Эрих Мария Ремарк",258 )
    print(book1)
    book2 = AudioBook("О дивный новый мир", "Олдос Хаксли", 11,54)
    print(book2)

