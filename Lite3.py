import sqlite3


class Db():
    __slots__ = ['__connection', '__cursor']

    def __init__(self):
        with sqlite3.connect('books.db') as self.__connection:
            self.__cursor = self.__connection.cursor()

    def __del__(self):
        self.__cursor.close()
        print('SQLite3')

    def commit(self):
        self.__connection.commit()

    def create_author_table(self):
        query = """CREATE TABLE IF NOT EXISTS author  (author_id 	INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_author VARCHAR(50) , 
                    UNIQUE(author_id,name_author) );"""

        self.__cursor.execute(query)

    def add_values_to_author_table(self):
        query = """INSERT INTO author (name_author)
                    VALUES('Булгаков М.А.'),('Достоевский Ф.М.'),
                    ('Есенин С.А.'),('Пастернак Б.Л.');"""

        self.__cursor.execute(query)
        self.commit()

    def create_book_table(self):
        query = """CREATE TABLE IF NOT EXISTS book (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    author_id INT NOT NULL,
    price DECIMAL(8,2),
    amount INT,
    FOREIGN KEY (author_id)  REFERENCES author (author_id) ON DELETE CASCADE ,
    UNIQUE( title,price,amount)
);"""

        self.__cursor.execute(query)
        self.commit()

    def add_values_to_book_table(self):
        query = """INSERT  INTO book (title,author_id,price,amount)
                    VALUES ('Стихотворения и поэмы',3,650.00,15),
                        ('Черный человек',3,570.20,6),
                        ('Лирика',4,518.99,2);"""

        self.__cursor.execute(query)
        self.commit()


if __name__ == '__main__':
    db = Db()
    db.create_author_table()
    db.create_book_table()
    db.add_values_to_author_table()
    db.add_values_to_book_table()
