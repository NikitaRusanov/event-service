from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse

import app.dto
import app.controllers.users


users_router = APIRouter(prefix='/users', tags=['users'])


@users_router.get('/{id}', response_model=app.dto.UserResponse, response_model_exclude={'password'})
def get_user(id: int) -> app.dto.UserResponse:
    """Returns user by id"""

    if res := app.controllers.users.get_user(id):
        return app.controllers.users.get_user(id)
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='Wrond user ID')


@users_router.post('/')
def create_user(user: app.dto.User) -> int:
    """Create new user, returns its id"""

    user_id = app.controllers.users.create_user(user) 
    return user_id


@users_router.put('/{id}')
def update_user(id: int, user: app.dto.User):
    """Change user information"""

    return app.controllers.users.update_user()


@users_router.delete('/{id}')
def delete_user(id: int):
    """Delete user"""
    return None