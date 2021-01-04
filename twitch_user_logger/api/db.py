import typing


class User:
    id: str
    broadcaster_type: str
    description: str
    display_name: str
    email: str
    login: str
    type: str
    view_count: str
    created_at: str


connection = sqlite3.connect('twitch_user.db')
database = connection.cursor()

def create_database() -> None:
    database.execute('''
        CREATE TABLE users (
            id text,
            broadcaster_type text,
            description text,
            display_name text,
            email text,
            login text,
            type text,
            view_count text,
            created_at text
        );
    ''')

    database.commit()


def insert_user(user: User) -> User:
    try:
        database.execute(f'''
            INSERT INTO users VALUES (
                    {user.id},
                    {user.broadcaster_type},
                    {user.description},
                    {user.display_name},
                    {user.email},
                    {user.login},
                    {user.type},
                    {user.view_count},
                    {user.created_at}
            );

        ''')

    except Exception as err:
        raise err

    return User


def user_exists(user_id: str) -> bool:
    database.execute(f'''
        SELECT id FROM users WHERE id=?';
    ''', (user_id,))

    if database.fetchone():
        return True

    return False
