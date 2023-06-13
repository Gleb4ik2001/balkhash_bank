# Python
import datetime

# Local
from database.core import Connection


class User:
    """Object from db. User."""

    id: int
    first_name: str
    last_name: str
    date_of_birth: datetime.datetime
    iin: str
    phone_number: str

    @staticmethod
    def create(
        conn: Connection,
        first_name: str,
        last_name: str,
        date_of_birth: datetime,
        iin: str,
        phone_number: str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO users(
                    first_name,
                    last_name,
                    date_of_birth,
                    iin,
                    phone_number
                )
                VALUES (
                    '{first_name}',
                    '{last_name}',
                    '{date_of_birth}',
                    '{iin}',
                    '{phone_number}'
                )
                """
            )
    @staticmethod
    def get(conn:Connection,**kwargs:dict[str,any])->"User":
        """
            SELECT * FROM users WHERE id =1 AND username = 'as'
        """
        condition:list[str]=[]
        for i in kwargs:
            if isinstance(kwargs[i],str):
                condition.append(f"{i} = '{kwargs[i]}'")
            else:
                condition.append(f"{i} = {kwargs[i]}")
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT * FROM users 
                WHERE {' AND '.join(condition)}
                LIMIT 1
            """)
            return cur.fetchone()

    @staticmethod
    def filter(conn:Connection,**kwargs:dict[str,any])->"User":
        """
            SELECT * FROM users WHERE id =1 AND username = 'as'
            WHERE id = 1
        """
        condition:list[str]=[]
        for i in kwargs:
            if isinstance(kwargs[i],str):
                condition.append(f"{i} = '{kwargs[i]}'")
            else:
                condition.append(f"{i} = {kwargs[i]}")
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT * FROM users 
                WHERE {' AND '.join(condition)}
            """)
            return cur.fetchall()
    @staticmethod
    def get_all(conn:Connection)->"User":
        query ="""
            SELECT * FROM users
        """
        with conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchall()
            print(result) 
            return result
    
    def inner_join(conn:Connection)->"User":
        query = """
            SELECT * FROM accounts
            INNER JOIN users ON users.id = accounts.owner_id
            INNER JOIN cards ON cards.account_id = accounts.id
            ;
        """
        with conn.cursor() as cur:
            cur.execute(query)
            print(cur.fetchall())
            return cur.fetchall()