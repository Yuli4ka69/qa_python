from conftest import setup_books, books


def test_get_list_of_favorites_books(setup_books, books):
    collector = setup_books
    assert books['book_1'] in collector.get_list_of_favorites_books()
