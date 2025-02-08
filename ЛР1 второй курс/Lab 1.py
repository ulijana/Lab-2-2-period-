from abc import ABC, abstractmethod
from typing import List, Any


class Furniture(ABC):
    """
    Абстрактный класс для описания мебели.
    """

    def __init__(self, material: str, dimensions: List[float]):
        """
        :param material: Материал, из которого изготовлена мебель (например, дерево, металл).
        :param dimensions: Размеры мебели в формате [длина, ширина, высота].
        :raises ValueError: Если размеры не положительные.
        """
        if any(dim <= 0 for dim in dimensions):
            raise ValueError("Все размеры должны быть положительными числами.")
        self.material = material
        self.dimensions = dimensions

    @abstractmethod
    def assemble(self) -> None:
        """
        Собрать мебель.
        """
        ...

    @abstractmethod
    def disassemble(self) -> None:
        """
        Разобрать мебель.
        """
        ...

    @abstractmethod
    def clean(self) -> None:
        """
        Очистить мебель.
        """
        ...


class SocialMediaPlatform(ABC):
    """
    Абстрактный класс для описания социальной платформы.
    """

    def __init__(self, name: str, user_count: int):
        """
        :param name: Название платформы.
        :param user_count: Количество пользователей на платформе.
        :raises ValueError: Если количество пользователей отрицательное.
        """
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.name = name
        self.user_count = user_count

    @abstractmethod
    def post(self, content: str) -> None:
        """
        Опубликовать контент на платформе.

        :param content: Содержимое публикации.
        :raises ValueError: Если содержимое пустое.
        """
        ...

    @abstractmethod
    def add_user(self, user_data: Any) -> None:
        """
        Добавить нового пользователя на платформу.

        :param user_data: Данные нового пользователя.
        """
        ...

    @abstractmethod
    def remove_user(self, user_id: int) -> None:
        """
        Удалить пользователя с платформы.

        :param user_id: Идентификатор пользователя.
        """
        ...


class Stack(ABC):
    """
    Абстрактный класс для описания структуры данных стек.
    """

    def __init__(self, max_size: int):
        """
        :param max_size: Максимальное количество элементов в стеке.
        :raises ValueError: Если максимальный размер меньше или равен нулю.
        """
        if max_size <= 0:
            raise ValueError("Максимальный размер должен быть положительным числом.")
        self.max_size = max_size
        self._stack: List[Any] = []

    @abstractmethod
    def push(self, item: Any) -> None:
        """
        Добавить элемент в стек.

        :param item: Элемент для добавления.
        :raises OverflowError: Если стек заполнен.
        """
        ...

    @abstractmethod
    def pop(self) -> Any:
        """
        Удалить и вернуть элемент с вершины стека.

        :return: Удаленный элемент.
        :raises IndexError: Если стек пуст.
        """
        ...

    @abstractmethod
    def peek(self) -> Any:
        """
        Вернуть элемент с вершины стека без удаления.

        :return: Элемент с вершины стека.
        :raises IndexError: Если стек пуст.
        """
        ...


if __name__ == "__main__":
    import doctest

    # Проверяем корректность реализации
    doctest.testmod()
