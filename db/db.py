import psycopg2
import asyncio
from dotenv import load_dotenv
import warnings
import os

load_dotenv()

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DB_NAME = os.environ.get("DB_NAME_PEOPLE")
DB_NAME_QUESTIONS = os.environ.get("DB_NAME_QUESTIONS")
DB_NAME_USERS = os.environ.get("DB_NAME_USERS")

warnings.simplefilter("always")


async def create_data_people():
    connection = None

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                F"""CREATE TABLE {DB_NAME}(
                        id INT,
                        name varchar(100),
                        second_name varchar(100),
                        patronymic varchar(100),
                        birth_data varchar(50),
                        death_data varchar(50),
                        birth_place varchar(100),
                        death_place varchar(100),
                        partner varchar(100),
                        kind varchar(100),
                        workplace varchar(100),
                        awards varchar(100),
                        epitaph varchar(10000),
                        biography_1 varchar(10000),
                        biography_2 varchar(10000),
                        biography_3 varchar(10000),
                        biography_4 varchar(10000),
                        word_familiar varchar(10000)
                        );
                        """
            )
        print("[INFO] Table created")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"


async def create_data_quesins():
    connection = None

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                F"""CREATE TABLE {DB_NAME_QUESTIONS}(
                        id INT,
                        question_1 varchar(10000),
                        question_2 varchar(10000),
                        question_3 varchar(10000),
                        question_4 varchar(10000),
                        question_5 varchar(10000),
                        question_6 varchar(10000),
                        question_7 varchar(10000),
                        question_8 varchar(10000),
                        question_9 varchar(10000),
                        question_10 varchar(10000));"""
            )
        print("[INFO] Table created")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"


async def create_data_users():
    connection = None

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                F"""CREATE TABLE {DB_NAME_USERS}(
                        id INT,
                        login varchar(100),
                        password varchar(100),
                        log_in BOOLEAN DEFAULT false
                        );
                        """
            )
        print("[INFO] Table created")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"


async def load_data_users(data):
    connection = None
    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO {DB_NAME_USERS} (id) VALUES (%s)", [data])

        print("[INFO] add info")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"

async def add_data_users(data):
    connection = None
    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE {DB_NAME_USERS} SET login = %s, password = %s,  log_in = true WHERE id = %s", data[1:] + [data[0]])

        print("[INFO] add info")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"

async def check_data(data):
    connection = None
    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {DB_NAME_USERS} WHERE id = %s", [data])

            print(cursor.rowcount)

            if cursor.rowcount == 0:
                if connection:
                    connection.close()

                return "false"
            else:
                a = cursor.fetchone()
                print(f"ID {a}")
                if a[-1]:
                    return "true"
                else:
                    return "false"


    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()


async def update_data(data):
    connection = None
    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE {DB_NAME_QUESTIONS} SET {list(data.keys())[1]} = %s WHERE id = %s", [data[list(data.keys())[1]], data["id"]])

        print("[INFO] add info")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        print(_ex)
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"

async def update_data_people(data):
    connection = None
    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            print(data, list(data.keys())[1:], [data["id"]])
            data["id"] = str(data["id"])
            cursor.execute(f"UPDATE {DB_NAME} SET {" ".join([ f"{i} = %s," for i in list(data.keys())[1:]])} WHERE id = %s", list(data.keys())[1:] + [data["id"]])

        print("[INFO] add info")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        print(_ex)
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"


async def load_data(data):
    connection = None
    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO {DB_NAME_QUESTIONS} (id) VALUES (%s)", data)

        print("[INFO] add info")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"


async def load_data_people(data):
    connection = None
    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO {DB_NAME} ({", ".join(list(data.keys()))}) VALUES ({", ".join(["%s"] * len(list(data.keys())))})",
                list(data.values()))

        print("[INFO] add info")

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return "ok"


async def return_data(id):
    connection = None
    return_ = ""

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {DB_NAME_QUESTIONS} WHERE id = %s", str(id))

            return_ = cursor.fetchone()
            print("Id: {}".format(return_))

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return return_


async def return_data_people(id):
    connection = None
    return_ = ""

    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {DB_NAME} WHERE id = %s", str(id))

            return_ = cursor.fetchone()
            print("Id: {}".format(return_))

    except Exception as _ex:
        warnings.warn(f"Error: {_ex}")
        return "error"

    finally:
        if connection:
            connection.close()

        return return_


if __name__ == '__main__':
    asyncio.run(add_data_users([0, "aba", "caba"]))
