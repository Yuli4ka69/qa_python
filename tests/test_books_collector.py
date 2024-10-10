import pytest

# Тест добавления новой книги
def test_add_new_book(collector, books):
    collector.add_new_book(books['book_1'])
    assert books['book_1'] in collector.books_genre  # Проверяем, что книга добавлена в коллекцию

# Тест добавления книги с длинным названием
def test_add_new_book_with_long_name(setup_books):
    long_name = 'a' * 41
    setup_books.add_new_book(long_name)
    assert long_name not in setup_books.get_books_genre()  # Книга не должна добавиться

# Тест добавления книги в избранное
def test_add_book_in_favorites(setup_books, books):
    setup_books.add_book_in_favorites(books['book_2'])
    assert books['book_2'] in setup_books.get_list_of_favorites_books()

# Тест удаления книги из избранного
def test_delete_book_from_favorites(favorite_books, books):
    favorite_books.delete_book_from_favorites(books['book_1'])
    assert books['book_1'] not in favorite_books.get_list_of_favorites_books()

# Тест получения списка избранных книг
def test_get_list_of_favorites_books(favorite_books, books):
    assert books['book_1'] in favorite_books.get_list_of_favorites_books()

# Тест получения книг, подходящих детям (без возрастных ограничений)
def test_get_books_for_children(setup_books, books):
    setup_books.set_book_genre(books['book_1'], 'Фантастика')
    setup_books.set_book_genre(books['book_2'], 'Детективы')  # Жанр с возрастным ограничением
    children_books = setup_books.get_books_for_children()
    assert books['book_1'] in children_books
    assert books['book_2'] not in children_books

# Тест получения словаря с книгами и их жанрами
def test_get_book_genre(setup_books, books):
    # Проверяем, что после добавления новой книги жанр пустой
    setup_books.add_new_book(books['book_1'])  # Добавляем новую книгу в коллекцию
    assert setup_books.get_book_genre(books['book_1']) == ''  # Жанр новой книги должен быть пустым

    # Устанавливаем жанр для этой книги
    setup_books.set_book_genre(books['book_1'], 'Фантастика')

    # Проверяем, что жанр книги теперь корректно установлен
    assert setup_books.get_book_genre(books['book_1']) == 'Фантастика'


# Тест получения книг с определённым жанром
def test_get_books_with_specific_genre(setup_books, books):
    setup_books.set_book_genre(books['book_1'], 'Фантастика')
    assert setup_books.get_books_with_specific_genre('Фантастика') == [books['book_1']]

# Параметризированный тест установки жанра книги
genres_data = [
    ('Гарри Поттер', 'Фантастика', 'Фантастика'),
    ('Шерлок Холмс', 'Детективы', 'Детективы'),
    ('Властелин Колец', 'Фантастика', 'Фантастика'),
    ('Прикольная книга', 'Комедии', 'Комедии')  # Изменено ожидаемое значение
]

@pytest.mark.parametrize("name, genre, expected_genre", genres_data)
def test_set_book_genre(setup_books, name, genre, expected_genre):
    setup_books.add_new_book(name)
    setup_books.set_book_genre(name, genre)  # Устанавливаем жанр для книги
    assert setup_books.get_book_genre(name) == expected_genre  # Проверяем, что жанр установлен правильно

# Тест установки жанра для несуществующей книги
def test_set_book_genre_for_nonexistent_book(setup_books):
    setup_books.set_book_genre('Несуществующая книга', 'Фантастика')
    assert setup_books.get_book_genre('Несуществующая книга') is None
