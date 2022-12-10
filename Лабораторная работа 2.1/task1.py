import doctest


class PythonCourses:
    def __init__(self, hours_amount: int, tasks_amount: int, lecturer: str):
        """
        Создание и подготовка к работе объекта "Курсы Python"
        :param hours_amount: Количество часов
        :param tasks_amount: Количество заданий
        :param lecturer: Лектор
        Примеры:
        >>> python_course = PythonCourses(360, 82, "Алексей Первушин")  # инициализация экземпляра класса
        """

        if not isinstance(hours_amount, int):
            raise TypeError("Количество часов быть типа int")
        if hours_amount <= 0:
            raise ValueError("Количество часов должно быть положительным числом")
        self.hours_amount = hours_amount

        if not isinstance(tasks_amount, int):
            raise TypeError("Количество заданий должно быть типа int")
        if tasks_amount <= 0:
            raise ValueError("Количество заданий должно быть положительным числом")
        self.tasks_amount = tasks_amount

        if not isinstance(lecturer, str):
            raise TypeError("Имя и фамилия лектора должны быть типа str")
        self.lecturer = lecturer

    def tasks_completion(self, solved_tasks: int) -> int:
        """
        Выполнение заданий
        :param solved_tasks: Выполненные задания
        :raise ValueError: Если введен не тип int, то вызываем ошибку
        :raise ValueError: Если количество выполненных заданий больше общего количества заданий, то вызываем ошибку
        :return: Общее количество выполненных заданий
        Примеры:
        >>> python_course = PythonCourses(360, 82, "Алексей Первушин")
        >>> python_course.tasks_completion(7)
        """
        ...

    def lecturer_change(self, new_lecturer: str) -> str:
        """
        Замена лектора
        :param new_lecturer: Имя и фамилия нового лектора
        :raise ValueError: Если введен не тип str, то вызываем ошибку
        :return: Имя и фамилия нового препода
        Примеры:
        >>> python_course = PythonCourses(360, 82, "Алексей Первушин")
        >>> python_course.lecturer_change("Иван Брык")
        """
        ...


class Hoodie:
    def __init__(self, size: int, colour: str):
        """
        Создание и подготовка к работе объекта "Худи"
        :param size: Размер
        :param colour: Цвет
        Примеры:
        >>> my_hoodie = Hoodie(50, "Чёрный")  # инициализация экземпляра класса
        """

        if not isinstance(size, int):
            raise TypeError("Размер должен быть типа int")
        if size < 28:
            raise ValueError("Размеры худи начинаются с 28-го размера")
        if size % 2 == 1:
            raise ValueError("Размеры худи - чётные числа")
        self.size = size

        if not isinstance(colour, str):
            raise TypeError("Цвет худи должен быть типа str")
        self.colour = colour

    def is_hoodie_clean(self) -> bool:
        """
        Функция проверяет, является ли худи чистым
        :return: Чистое ли худи
        Примеры:
        >>> my_hoodie = Hoodie(50, "Чёрный")
        >>> my_hoodie.is_hoodie_clean()
        """
        ...

    def sew_in_hoodie(self, sewed_size: int) -> int:
        """
        Ушивание худи
        :param sewed_size: На сколько размеров ушивается худи
        :raise ValueError: Если введен не тип int, то вызываем ошибку
        :raise ValueError: Если ушив выполняется на отрицательный размер, то вызываем ошибку
        :raise ValueError: Если ушив выполняется на размер больший, чем само худи, то вызываем ошибку
        :return: Размер худи после ушива
        Примеры:
        >>> my_hoodie = Hoodie(50, "Чёрный")
        >>> my_hoodie.sew_in_hoodie(4)
        """
        ...


class Mp3Player:
    def __init__(self, memory_size_gb: (int, float), colour: str, display_presence: bool):
        """
        Создание и подготовка к работе объекта "MP3-плеер"
        :param memory_size_gb: Объём памяти в Гигабайтах
        :param colour: Цвет
        :param display_presence: Наличие дисплея

        Примеры:
        >>> mp3_player = Mp3Player(4, "Чёрный", True)  # инициализация экземпляра класса
        """

        if not isinstance(memory_size_gb, (int, float)):
            raise TypeError("Объём памяти должен быть быть типа int")
        if memory_size_gb <= 0:
            raise ValueError("Объём памяти должен быть положительным числом")
        self.memory_size_gb = memory_size_gb

        if not isinstance(colour, str):
            raise TypeError("Цвет плеера должен быть типа str")
        self.colour = colour

        if not isinstance(display_presence, bool):
            raise TypeError("Значение должно быть True или False")

    def memory_boost(self, memory_increase: int) -> int:
        """
        Ушивание худи
        :param memory_increase: На сколько гиигабайт увеличивается память
        :raise ValueError: Если введен не тип int, то вызываем ошибку
        :raise ValueError: Если введено не положительное значние, то вызываем ошибку
        :return: Объём памяти после увеличения
        Примеры:
        >>> mp3_player = Mp3Player(4, "Чёрный", True)
        >>> mp3_player.memory_boost(4)
        """
        ...

    def color_change(self, new_color: str) -> str:
        """
        Ушивание худи
        :param new_color: Новый цвет
        :raise ValueError: Если введен не тип str, то вызываем ошибку
        :return: Новый цвет
        Примеры:
        >>> mp3_player = Mp3Player(4, "Чёрный", True)
        >>> mp3_player.color_change("Красный")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
