# Python
from decouple import config
import datetime

# Local
from database.core import Connection
from database.models.users import User
from database.models.cards import Card
from database.models.accounts import Account


my_connection: Connection = Connection(
    host=config('DB_HOST', str),
    port=config('DB_PORT', int),
    user=config('DB_USER', str),
    password=config('DB_PASSWORD', str),
    dbname=config('DB_NAME', str)
)

if __name__ == '__main__':
    my_connection.create_tables()
    # User.create(
    #     conn=my_connection.conn,
    #     first_name='Bob',
    #     last_name='Flint',
    #     date_of_birth=datetime.datetime(
    #         year=1998,
    #         month=5,
    #         day=15
    #     ),
    #     iin='980515223534',
    #     phone_number='7009056050'
    # )
    # Card.create(
    #     conn=my_connection.conn,
    #     number="1234432112513245",
    #     account_id = "2",
    #     cvv='124',
    #     pin='1432',
    #     is_active=True,
    #     date_end = datetime.datetime(
    #         year=2021,
    #         month=6,
    #         day = 3
    #     )
    # )
    # Account.create(
    #     conn=my_connection.conn,
    #     number='12345fdgtrq3213454rf',
    #     owner=2,
    #     balance="2200",
    #     my_type='123f'
    # )


    # print(User.get_all(conn=my_connection.conn))


    # print(User.filter(conn=my_connection.conn,first_name = "Bob"))

    print(User.inner_join(conn=my_connection.conn))


    
