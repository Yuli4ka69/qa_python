def test_add_new_book(collector, books):
    collector.add_new_book(books['book_1'])
    assert books['book_1'] in collector.books_genre  # Проверяем, что книга добавлена в коллекцию
