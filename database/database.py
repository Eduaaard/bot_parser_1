import psycopg2
from config import DB_USER, DB_HOST, DB_NAME, DB_PASSWORD


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                fetchmany: bool = False,
                commit: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchmany:
                    result = cursor.fetchmany()
            return result


class TableCreator(DataBase):
    def create_users_table(self):
        sql = """
            DROP TABLE IF EXISTS users;
            CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name TEXT,
                phone_number TEXT,
                chat_id BIGINT NOT NULL UNIQUE
            );
        """
        self.manager(sql, commit=True)


class UserManager(DataBase):
    """Работа с таблицей пользователя."""

    def get_user_id(self, chat_id):
        sql = "SELECT user_id FROM users WHERE chat_id = %s;"
        return self.manager(sql, chat_id, fetchone=True)

    def add_user(self, name, phone_number, chat_id):
        sql = "INSERT INTO users(name, phone_number, chat_id) VALUES (%s, %s, %s);"
        self.manager(sql, name, phone_number, chat_id, commit=True)


class MainManager:
    def __init__(self):
        self.user: UserManager = UserManager()


# creator = TableCreator()
# creator.create_users_table()

