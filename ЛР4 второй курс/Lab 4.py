from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Конструктор класса Animal.
        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self._name = name  # Инкапсуляция имени, так как изменение имени должно происходить через методы
        self._age = age  # Инкапсуляция возраста, чтобы предотвратить некорректные изменения

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного.
        """
        return f"Животное: {self._name}, возраст: {self._age} лет"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки.
        """
        return f"Animal(name={self._name}, age={self._age})"

    @abstractmethod
    def make_sound(self) -> str:
        """
        Абстрактный метод для звука животного.
        """
        pass


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Dog.
        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self._breed = breed  # Инкапсулированный атрибут, так как порода не должна меняться после создания объекта

    def __str__(self) -> str:
        """
        Перегруженный метод __str__, чтобы добавить информацию о породе.
        """
        return f"Собака: {self._name}, порода: {self._breed}, возраст: {self._age} лет"

    def __repr__(self) -> str:
        """
        Перегруженный метод __repr__, чтобы добавить информацию о породе.
        """
        return f"Dog(name={self._name}, age={self._age}, breed={self._breed})"

    def make_sound(self) -> str:
        """
        Реализация метода make_sound.
        """
        return "Гав-гав!"

    def fetch(self) -> str:
        """
        Метод, который показывает способность собаки приносить предметы.
        """
        return f"{self._name} принес мяч!"


if __name__ == "__main__":
    dog = Dog("Бобик", 3, "Лабрадор")
    print(dog)  # Собака: Бобик, порода: Лабрадор, возраст: 3 лет
    print(dog.make_sound())  # Гав-гав!
    print(dog.fetch())  # Бобик принес мяч!
    print(repr(dog))  # Dog(name=Бобик, age=3, breed=Лабрадор)
