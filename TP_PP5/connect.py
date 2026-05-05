import mysql.connector
from mysql.connector import Error
from data import DB


def get_connection():
    """
    Créé et retourne une nouvelle connexion MYSQL.
    Léve une exception si la connexion échoue
    """
    try:
        connection = mysql.connector.connect(**DB)
        return connection
    except Error as e:
        print(f"Erreur connexion Mysql : {e}")
        raise
    