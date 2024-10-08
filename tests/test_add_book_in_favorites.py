def test_add_book_in_favorites(setup_books, books):
    collector = setup_books
    collector.add_book_in_favorites(books['book_2'])
    assert books['book_2'] in collector.get_list_of_favorites_books()
