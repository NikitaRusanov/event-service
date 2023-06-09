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
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='User not found')


@users_router.post('/')
def create_user(user: app.dto.User) -> int:
    """Create new user, returns its id"""

    user_id = app.controllers.users.create_user(user) 
    return user_id


@users_router.put('/{id}', response_model=app.dto.UserResponse, response_model_exclude={'password'})
def update_user(id: int, user: app.dto.User):
    """Change user information"""

    res = app.controllers.users.update_user(id, user)

    if res == app.dto.ResultCode.NOT_FOUND:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='User not found')
    if res == app.dto.ResultCode.WRONG_PASS:
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content='Wrong password')
    return res
    


@users_router.delete('/{id}', response_model=app.dto.UserResponse, response_model_exclude={'password'})
def delete_user(id: int):
    """Delete user"""
    
    if res := app.controllers.users.delete_user(id):
        return res
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='User not found')



