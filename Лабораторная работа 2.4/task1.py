import doctest


class Shoes:
    """ Базовый класс Обувь """

    def __init__(self, size: int, material: str):
        """
        Создание и подготовка к работе объекта "Обувь"
        :param size: Размер обуви
        :param material: Материал
        Примеры:
        >>> my_shoes = Shoes(42, "Искусственная кожа")  # инициализация экземпляра класса
        """
        self._size = size
        self._material = material

    def __str__(self):
        return f"Обувь {self.size}-го размера из материала: {self.material}"

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self._size!r}, material={self._material!r})"

    @property
    def size(self) -> int:
        """
        Непубличный атрибут, так как невозможно изменить размер обуви
        :return: Размер обуви
        """
        return self._size


    @property
    def material(self) -> str:
        """
        Непубличный атрибут, так как невозможно изменить материал обуви
        :return: Материал обуви
        """
        return self._material


class Sneakers(Shoes):
    """Дочерний класс Кроссовки"""

    def __init__(self, size: int, material: str, laces_color: str):
        """
        Создание и подготовка к работе объекта "Кроссовки"
        :param size: Размер обуви
        :param material: Материал
        :param laces_color: Цвет шнурков
        Примеры:
        >>> my_sneakers = Sneakers(37, "Текстиль", "Синий")  # инициализация экземпляра дочернего класса
        """
        super().__init__(size, material)
        self.laces_color = laces_color

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, new_color: str) -> None:
        """
        Замена шнурков
        :param new_color: Новый цвет шнурков
        :raise TypeError: Если введён не тип str, то вызываем ошибку
        Примеры:
        >>> my_sneakers = Sneakers(37, "Текстиль", "Синий")
        >>> sneakers.laces_color = "Желтый"
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет шнурков должен быть типа str")
        self.laces_color = new_color

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self.size!r}, material={self.material!r}, " \
               f"laces color={self.laces_color!r})"


class Boots(Shoes):
    """Дочерний класс Ботинки"""

    def __init__(self, size: int, material: str, season: str):
        """
        Создание и подготовка к работе объекта "Ботинки"
        :param size: Размер обуви
        :param material: Материал
        :param season: Сезон
        Примеры:
        >>> my_boots = Boots(42, "Натуральная кожа", "Осень")  # инициализация экземпляра класса
        """
        super().__init__(size, material)
        self.season = season

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self.size!r}, material={self.material!r}, season={self.season!r})"


shoes = Shoes(48, "Искусственная кожа")
sneakers = Sneakers(37, "Текстиль", "Синий")
boots = Boots(42, "Натуральная кожа", "Осень")
print(shoes)
print(sneakers.laces_color)
print(boots.season)

if __name__ == "__main__":
    doctest.testmod()
    pass
