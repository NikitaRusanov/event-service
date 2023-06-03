from fastapi import APIRouter

import app.dto


users_router = APIRouter(prefix='/users', tags=['users'])


@users_router.get('/{id}')
def get_user(id: int) -> app.dto.User:
    """Returns user by id"""
    return None


@users_router.post('/')
def create_user(user: app.dto.User) -> int:
    """Create new user, returns its id"""
    return None


@users_router.put('/{id}')
def update_user(id: int, user: app.dto.User):
    """Change user information"""
    return None


@users_router.delete('/{id}')
def delete_user(id: int):
    """Delete user"""
    return None