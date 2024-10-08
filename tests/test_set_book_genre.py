import pytest
from conftest import setup_books, books

# Данные для параметризации
genres_data = [
    ('Гарри Поттер', 'Фантастика', 'Фантастика'),
    ('Шерлок Холмс', 'Детективы', 'Детективы'),
    ('Властелин Колец', 'Фантастика', 'Фантастика'),
    ('Прикольная книга', 'Комедии', 'Комедии')  # Изменено ожидаемое значение
]

@pytest.mark.parametrize("name, genre, expected_genre", genres_data)
def test_set_book_genre(setup_books, name, genre, expected_genre):
    collector = setup_books
    # Добавляем книгу в коллекцию, если её там нет
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)  # Устанавливаем жанр для книги
    assert collector.get_book_genre(name) == expected_genre  # Проверяем, что жанр установлен правильно
