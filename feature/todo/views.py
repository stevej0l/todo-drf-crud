from .models import Todo
from .dataclasses import TodoData


def list_todos():
    return Todo.objects.all().order_by("-created_at")


def get_todo(todo_id: int):
    return Todo.objects.get(id=todo_id)


def create_todo(todo_data: TodoData):
    return Todo.objects.create(
        title=todo_data.title,
        description=todo_data.description,
        is_completed=todo_data.is_completed,
    )


def update_todo(todo: Todo, todo_data: TodoData):
    todo.title = todo_data.title
    todo.description = todo_data.description
    todo.is_completed = todo_data.is_completed
    todo.save()
    return todo


def delete_todo(todo: Todo):
    todo.delete()