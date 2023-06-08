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