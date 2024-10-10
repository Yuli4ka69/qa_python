import pytest
from main import BooksCollector  # Импортируем тестируемый класс

# Фикстура для создания нового экземпляра BooksCollector с областью видимости 'function'
@pytest.fixture(scope='function')
def collector():
    return BooksCollector()

# Фикстура для добавления нескольких книг в коллекцию
@pytest.fixture
def books():
    return {
        'book_1': 'Гарри Поттер',
        'book_2': 'Шерлок Холмс',
        'book_3': 'Властелин Колец',
        'book_4': 'Неизвестная книга'
    }

# Фикстура для списка жанров книг с областью видимости 'module'
@pytest.fixture(scope='module')
def genres():
    return ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

# Фикстура для добавления книг в коллекцию перед тестами
@pytest.fixture
def setup_books(collector, books):
    for book in books.values():
        collector.add_new_book(book)
    return collector

# Фикстура для автоматического добавления книги в избранное
@pytest.fixture
def favorite_books(setup_books, books):
    setup_books.add_book_in_favorites(books['book_1'])
    return setup_books
