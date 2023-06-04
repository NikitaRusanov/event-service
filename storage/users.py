from storage.db_manager import session
import storage.models


def create_user(name: str, email: str, password: str) -> int:
    user_id = None

    with session() as db:
        user = storage.models.User(
            name=name,
            email=email,
            password=password
        )
        db.add(user)

        user_id = user.id
        db.commit()

    return user_id


def get_user(id: int) -> storage.models.User | None:
    with session() as db:
        return db.get(storage.models.User, id)
