import sqlite3


CREATE_ALBUM_TABLE = "CREATE TABLE IF NOT EXISTS album (id INTEGER PRIMARY KEY, name TEXT, top TEXT, rating INTEGER)"

INSERT_ALBUMS = "INSERT INTO album (name, top, rating) VALUES (?, ?, ?);"

GET_ALL_ALBUMS = "SELECT * FROM album"
GET_ALBUMS_BY_NAME = "SELECT * FROM album WHERE name = ?;"
GET_TOP_SONGS_OF_ALBUM = """
SELECT * FROM album
WHERE name = ?
ORDER BY rating DESC;"""
REMOVE_ALBUM = "DELETE FROM album WHERE name = ?;"
ORDER_ALBUMS_BY_NAME = """
SELECT * FROM album 
ORDER BY name ASC;"""


def connect():
    return sqlite3.connect("album.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_ALBUM_TABLE)


def add_album(connection, name, top, rating):
    with connection:
        connection.execute(INSERT_ALBUMS, (name, top, rating))


def get_all_albums(connection):
    with connection:
        return connection.execute(GET_ALL_ALBUMS).fetchall()


def get_albums_by_name(connection, name):
    with connection:
        return connection.execute(GET_ALBUMS_BY_NAME, (name,)).fetchall()


def get_top_songs_of_album(connection, name):
    with connection:
        return connection.execute(GET_TOP_SONGS_OF_ALBUM, (name,)).fetchall()


def remove_album(connection, name):
    with connection:
        return connection.execute(REMOVE_ALBUM, (name,))


def order_album(connection):
    with connection:
        return connection.execute(ORDER_ALBUMS_BY_NAME).fetchall()
