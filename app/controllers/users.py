import app.dto

import storage.users


def create_user(user: app.dto.User) -> int:
    user_id = storage.users.create_user(
        name=user.name,
        email=user.email,
        password=user.password
    )

    return user_id


def get_user(id: int) -> app.dto.UserResponse:
    user = storage.users.get_user(id)

    return user


def update_user(id: int, user: app.dto.User) -> app.dto.User | None:
    res = storage.users.update_user(
        id=id,
        name = user.name,
        email=user.email,
        password=user.password
    )

    return user if res else None