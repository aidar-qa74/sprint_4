# qa_python
1 - test_add_new_book_valid_name(self, collector): Тест добавления книги с корректным названием (до 40 символов)

2 - def test_add_new_book_invalid_name(self, collector, book_name): Tест добавления книги с некорректным названием (пустая строка или >40 символов)

3 - def test_add_new_book_duplicate(self, collector): Тест попытки добавить книгу, которая уже есть в коллекции
    
4 - def test_set_book_genre_valid(self, collector): Тест установки корректного жанра для существующей книги
    
5 - def test_set_book_genre_invalid_book(self, collector): Тест установки жанра для книги, которой нет в коллекции

6 - def test_set_book_genre_invalid_genre(self, collector): Тест установки некорректного жанра (не в списке genre)
      
7 - def test_get_books_with_specific_genre(self, collector, genre, expected_books): Тест получения списка книг определённого жанра
       
8 - def test_get_books_for_children(self, collector): Тест получения книг, подходящих детям (без возрастного рейтинга)
       
9 - def test_add_book_in_favorites_valid(self, collector): Тест добавления книги в избранное (книга есть в коллекции)
       
10 - def test_add_book_in_favorites_invalid(self, collector): Тест попытки добавить в избранное книгу, которой нет в коллекции
        
11 - def test_delete_book_from_favorites(self, collector): Тест удаления книги из избранного
        