import MySQLdb as mariadb
from db_info import movie_host, movie_user, movie_password, movie_db


def connect_to_database(host=movie_host, user=movie_user, password=movie_password, db=movie_db):
    """Connects to a database using the provided credentials"""

    db_connection = mariadb.connect(host, user, password, db)
    return db_connection


def execute_query(db_connection=None, query=None, query_params=None):
    """Executes the query on the database using the provided query paramaters

    Args:
        db_connection: The database. Defaults to None.
        query: The query that will be executed on the database. Defaults to None.
        query_params: The parameters for the provided query. Defaults to None.

    Returns:
        [type]: [description]
    """
    if db_connection is None:
        print("No connection to the database found! Have you called connect_to_database() first?")
        return None

    if query is None or len(query.strip()) == 0:
        print("Query is empty. Please enter a valid SQL Query")
        return None

    print("Executing {query} using {query_params}")

    cursor = db_connection.cursor()
    cursor.execute(query, query_params)
    db_connection.commit()
    return cursor


if __name__ == "__main__":
    pass
