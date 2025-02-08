class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        id (int): Идентификатор книги.
        name (str): Название книги.
        pages (int): Количество страниц в книге.
    """

    def __init__(self, id_, name, pages):
        """
        Инициализирует экземпляр книги.

        Аргументы:
            id_ (int): Идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строковое представление книги в формате 'Книга "Название"'.
        """
        return f'\u041a\u043d\u0438\u0433\u0430 "{self.name}"'

    def __repr__(self):
        """
        Возвращает строку, которая может быть использована для воссоздания объекта.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# База данных книг
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    },
]

if __name__ == '__main__':
    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Проверяем метод __str__
    for book in list_books:
        print(book)

    # Проверяем метод __repr__
    print(list_books)




