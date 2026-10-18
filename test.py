from main import BooksCollector
import pytest

class TestBooksCollector:  
    @pytest.fixture

    def collector(self):
       # Фикстура для создания объекта BooksCollector перед каждым тестом
        return BooksCollector()

    def test_add_new_book_valid_name(self, collector):
       # Тест добавления книги с корректным названием (до 40 символов)
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre
        assert collector.books_genre["Война и мир"] == ''

    @pytest.mark.parametrize("book_name", [
        "",  # пустая строка
        "a" * 41  # строка из 41 символа
    ])
    def test_add_new_book_invalid_name(self, collector, book_name):
       # Tест добавления книги с некорректным названием (пустая строка или >40 символов)
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_add_new_book_duplicate(self, collector):
        #Тест попытки добавить книгу, которая уже есть в коллекции.
        collector.add_new_book("Преступление и наказание")
        collector.add_new_book("Преступление и наказание")  # повторная попытка
        assert len(collector.books_genre) == 1

    def test_set_book_genre_valid(self, collector):
        #Тест установки корректного жанра для существующей книги.
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

    def test_set_book_genre_invalid_book(self, collector):
        #Тест установки жанра для книги, которой нет в коллекции.
        collector.set_book_genre("Неизвестная книга", "Ужасы")
        assert collector.get_book_genre("Неизвестная книга") is None

    def test_set_book_genre_invalid_genre(self, collector):
        #Тест установки некорректного жанра (не в списке genre).
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Поэзия")  # "Поэзия" нет в self.genre
        assert collector.get_book_genre("1984") == ''

    @pytest.mark.parametrize("genre, expected_books", [
        ("Фантастика", ["Гарри Поттер"]),
        ("Ужасы", []),  # в коллекции нет книг этого жанра
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected_books):
       # Тест получения списка книг определённого жанра.
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")

        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_books

    def test_get_books_for_children(self, collector):
        #Тест получения книг, подходящих детям (без возрастного рейтинга)
        # Добавляем книги разных жанров
        collector.add_new_book("Мульт про смешариков")
        collector.set_book_genre("Мульт про смешариков", "Мультфильмы")

        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")  # есть возрастной рейтинг

        result = collector.get_books_for_children()
        assert "Мульт про смешариков" in result
        assert "Шерлок Холмс" not in result

    def test_add_book_in_favorites_valid(self, collector):
        #Тест добавления книги в избранное (книга есть в коллекции)
        collector.add_new_book("Маленький принц")
        collector.add_book_in_favorites("Маленький принц")
        assert "Маленький принц" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_invalid(self, collector):
        #Тест попытки добавить в избранное книгу, которой нет в коллекции
        collector.add_book_in_favorites("Неизвестная книга")
        assert "Неизвестная книга" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
       # Тест удаления книги из избранного
        collector.add_new_book("Убить пересмешника")
        collector.add_book_in_favorites("Убить пересмешника")

        collector.delete_book_from_favorites("Убить пересмешника")
        assert "Убить пересмешника" not in collector.get_list_of_favorites_books()
        