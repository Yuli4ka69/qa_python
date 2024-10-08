def test_add_new_book_with_long_name(setup_books):
    collector = setup_books
    long_name = 'a' * 41
    collector.add_new_book(long_name)
    assert long_name not in collector.get_books_genre()  # Книга не должна добавиться
