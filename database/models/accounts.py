# Local
from database.core import Connection
from database.models.users import User


class Account:
    """Object from db. Accounts"""

    id: int
    number: str
    owner: User
    balance: str
    my_type: str

    @staticmethod
    def create(
        conn: Connection,
        number: str,
        owner: int,
        balance: str,
        my_type: str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO accounts(
                    number,
                    owner_id,
                    balance,
                    type
                )
                VALUES (
                    '{number}',
                    '{owner}',
                    '{balance}',
                    '{my_type}'
                )
                """
            )