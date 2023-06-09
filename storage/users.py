from storage.db_manager import session
import storage.models

import app.dto


def create_user(name: str, email: str, password: str) -> int:
    user_id = -1

    with session() as db:
        user = storage.models.User(
            name=name,
            email=email,
            password=password
        )

        db.add(user)
        db.commit()

        user_id = user.id

    return user_id


def get_user(id: int) -> app.dto.UserResponse | None:
    with session() as db:
        result =  db.get(storage.models.User, id)
        result = app.dto.UserResponse.from_orm(result) if result else None
    
    return result
        


def update_user(id: int, name: str | None = None, email: str | None = None, password: str | None = None) -> bool:
    with session() as db:
        if user := db.get(storage.models.User, id):
            user.name = name if name else user.name
            user.email = email if email else user.email
            user.password = password if password else user.password
            return True
    
    return False
        

def delete_user(id: int) -> bool:
    with session() as db:
        if user := db.get(storage.models.User, id):
            db.delete(user)
            db.commit()
            return True
        else:
            return False
    