def test_get_books_for_children(setup_books, books):
    collector = setup_books
    collector.set_book_genre(books['book_1'], 'Фантастика')
    collector.set_book_genre(books['book_2'], 'Детективы')  # Жанр с возрастным ограничением
    assert collector.get_books_for_children
