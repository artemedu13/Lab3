class Bicycle:
    def __int__(self, frame_size: int, number_of_shock_absorbers: int):
        """
        Подготовка объекта "Велосипед"
        :param frame_size: Размер рамы
        :param number_of_shock_absorbers: Кол-во амортизаторов
        """
        self._frame_size = frame_size
        self._number_of_shock_absorbers = number_of_shock_absorbers

    @property
    def frame_size(self):
        return self._frame_size

    @frame_size.setter
    def frame_size(self, frame_size: int):
        if not isinstance(frame_size, int):
            raise TypeError("Размер рамы должен быть int")
        if frame_size < 13:
            raise ValueError("Минимальный размер рамы 13")
        if frame_size > 24:
            raise ValueError("Максимальный размер рамы 24")
        self._frame_size = frame_size

    @property
    def number_of_shock_absorbers(self):
        return self._number_of_shock_absorbers

    @number_of_shock_absorbers.setter
    def number_of_shock_absorbers(self, number_of_shock_absorbers: int):
        if not isinstance(number_of_shock_absorbers, int):
            raise TypeError("Кол-во должно быть int")
        if number_of_shock_absorbers < 1:
            raise ValueError("Минимальное кол-во амортизаторов 1")
        if number_of_shock_absorbers > 2:
            raise ValueError("Максимальное кол-во амортизаторов 2")
        self._number_of_shock_absorbers = number_of_shock_absorbers

    def __str__(self):
        return f"Размер рамы {self._frame_size}. Количество амортизаторов {self._number_of_shock_absorbers}"

    def __repr__(self):
        return f"{self.__class__.__name__}(frame_size={self._frame_size!r}, number_of_shock_absorbers={self._number_of_shock_absorbers!r})"

    def price(self):
        """
        Возвращает стоимость относительно размера рамы и кол-во амортизаторов
        :return: Стоимость велосипеда
        """


class ElectroBicycle(Bicycle):
    def __int__(self, frame_size: int, number_of_shock_absorbers: int, number_of_electric_motors: int):
        super().__init__(frame_size, number_of_shock_absorbers)
        """
        Подготовка объекта "Электровелосипед"
        :param frame_size: Размер рамы
        :param number_of_shock_absorbers: Кол-во амортизаторов
        :param number_of_electric_motors: Кол-во электродвигателей
        Наследуем размер рамы и кол-во амортизаторов, добавляем параметр кол-во электродвигателей
        """
        self._number_of_electric_motors = number_of_electric_motors

    @property
    def number_of_electric_motors(self):
        return self._number_of_electric_motors

    @number_of_electric_motors.setter
    def number_of_electric_motors(self, number_of_electric_motors: int):
        if not isinstance(number_of_electric_motors, int):
            raise TypeError("Кол-во должно быть int")
        if number_of_electric_motors < 1:
            raise ValueError("Минимальное кол-во электродвигателей 1")
        if number_of_electric_motors > 2:
            raise ValueError("Максимальное кол-во электродвигателей 2")
        self._number_of_electric_motors = number_of_electric_motors

    def __str__(self):
        return f"Размер рамы {self._frame_size}, Количество амортизаторов {self._number_of_shock_absorbers}, Количество электродвигателей {self._number_of_electric_motors}"

    def __repr__(self):
        return f"{self.__class__.__name__}(frame_size={self._frame_size!r}, number_of_shock_absorbers={self._number_of_shock_absorbers!r}, number_of_electric_motors={self._number_of_electric_motors!r})"

    def price(self):
        """
        Перезагружаем стоимость с учетом электродвигателя
        :return: Стоимость велосипеда
        """


if __name__ == "__main__":
    pass
#Конец