from fastapi import APIRouter, Body

import app.dto
import app.controllers.users


users_router = APIRouter(prefix='/users', tags=['users'])


@users_router.get('/{id}', response_model=app.dto.UserResponse, response_model_exclude={'password'})
def get_user(id: int) -> app.dto.UserResponse:
    """Returns user by id"""
    
    return app.controllers.users.get_user(id)


@users_router.post('/')
def create_user(user: app.dto.User) -> int:
    """Create new user, returns its id"""

    user_id = app.controllers.users.create_user(user) 
    return user_id


@users_router.put('/{id}')
def update_user(id: int, user: app.dto.User):
    """Change user information"""
    return None


@users_router.delete('/{id}')
def delete_user(id: int):
    """Delete user"""
    return None