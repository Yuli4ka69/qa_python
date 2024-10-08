def test_get_books_genre(setup_books, books):
    collector = setup_books
    collector.add_new_book(books['book_1'])  # Добавляем книгу перед установкой жанра
    collector.set_book_genre(books['book_1'], 'Фантастика')  # Устанавливаем жанр
    assert collector.get_books_genre() == {books['book_1']: 'Фантастика'}
