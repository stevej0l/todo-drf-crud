from django.urls import path
from .controllers import (
    create_todo_controller,
    list_todos_controller,
    get_todo_controller,
    update_todo_controller,
    delete_todo_controller,
)

urlpatterns = [
    path("todos/create/", create_todo_controller),
    path("todos/list/", list_todos_controller),
    path("todos/get/", get_todo_controller),
    path("todos/update/", update_todo_controller),
    path("todos/delete/", delete_todo_controller),
]
