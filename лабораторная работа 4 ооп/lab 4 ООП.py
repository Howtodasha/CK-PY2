class Pets:
    """Описываем базовый класс"""
    def __init__(self, size: str):
        self.size = size
    """Метод описывает размер домашнего животного"""

    def __str__(self) -> str:
        return f'размер домашнего животного {self.size}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}" \
               f"(size={self.size!r})"


class Dogs(Pets):
    """Описываем дочерний класс"""
    def __init__(self, size: str, breed: str):
        super().__init__(size)
        self.breed = breed
        if not isinstance(breed, str):
            raise TypeError(f'{self.breed} должна быть указана порода')
    """Метод описывает породу наследуемого класса животного"""

    def __str__(self):
        super_str = super().__str__()
        return f'{super_str}. порода {self.breed}'

    def __repr__(self):
        super_repr = super().__repr__()
        return f"{super_repr}, (breed={self.breed!r})"


if __name__ == "__main__":
    husky = Dogs("большой", "хаски")
    print(husky)
    pass
