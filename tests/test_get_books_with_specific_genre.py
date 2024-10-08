from conftest import setup_books, books


def test_get_books_with_specific_genre(setup_books, books):
    collector = setup_books
    collector.set_book_genre(books['book_1'], 'Фантастика')
    assert collector.get_books_with_specific_genre('Фантастика') == [books['book_1']]
