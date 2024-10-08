from conftest import setup_books


def test_set_book_genre_for_nonexistent_book(setup_books):
    collector = setup_books
    collector.set_book_genre('Несуществующая книга', 'Фантастика')
    assert collector.get_book_genre('Несуществующая книга') is None
