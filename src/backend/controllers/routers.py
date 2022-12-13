from fastapi.routing import APIRouter
from .base import app

from . import auth, tasks, users, answer, question

app_router = APIRouter(prefix='')

app_router.include_router(answer.router, prefix='/answer', tags=['answer'])
app_router.include_router(auth.router, prefix='', tags=['auth'])
app_router.include_router(tasks.router, prefix='/tasks', tags=['tasks'])
app_router.include_router(users.router, prefix='/users', tags=['users'])
app_router.include_router(question.router, prefix='/questions', tags=['questions'])


'''
from .misc import *
from .result import *
from .child_results import *
'''

app.include_router(app_router)

