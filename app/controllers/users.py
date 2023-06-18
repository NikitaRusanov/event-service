import app.dto

import storage.users
import storage.events


def create_user(user: app.dto.User) -> int:
    user_id = storage.users.create_user(
        name=user.name,
        email=user.email,
        password=user.password
    )

    return user_id


def get_user(id: int) -> app.dto.UserResponse | None:
    user = storage.users.get_user(id)

    return user


def update_user(id: int, user: app.dto.User) -> app.dto.User | app.dto.ResultCode:
    user_db = storage.users.get_user(id)

    if not user_db:
        return app.dto.ResultCode.NOT_FOUND

    if user_db.password != user.password:
        return app.dto.ResultCode.WRONG_PASS

    res = storage.users.update_user(
        id=id,
        name=user.name,
        email=user.email,
    )

    return res if res else app.dto.ResultCode.NOT_FOUND


def delete_user(id: int) -> app.dto.UserResponse | None:
    user = storage.users.get_user(id)
    res = storage.users.delete_user(id)

    if res:
        return user
    return None


def subscribe(user_id: int, event_id: str) -> app.dto.UserResponse | app.dto.ResultCode:
    if not storage.users.get_user(user_id):
        return app.dto.ResultCode.USER_NOT_FOUND
    if not storage.events.read_events(event_id):
        return app.dto.ResultCode.EVENT_NOT_FOUND

    return storage.users.subscribe(user_id, event_id)
