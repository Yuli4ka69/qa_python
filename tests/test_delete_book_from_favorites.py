from conftest import setup_books, books


def test_delete_book_from_favorites(setup_books, books):
    collector = setup_books
    collector.add_book_in_favorites(books['book_2'])
    collector.delete_book_from_favorites(books['book_2'])
    assert books['book_2'] not in collector.get_list_of_favorites_books()
