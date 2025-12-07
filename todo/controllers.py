from dataclasses import asdict
from typing import List

from django.shortcuts import get_object_or_404

from .models import Todo
from .dataclasses import TodoData, TodoUpdateData


def list_todos() -> List[Todo]:
    return Todo.objects.all().order_by("-created_at")


def get_todo(todo_id: int) -> Todo:
    return get_object_or_404(Todo, id=todo_id)


def create_todo(data: TodoData) -> Todo:
    return Todo.objects.create(**asdict(data))


def update_todo(todo_id: int, data: TodoUpdateData) -> Todo:
    todo = get_todo(todo_id)

    if data.title is not None:
        todo.title = data.title
    if data.description is not None:
        todo.description = data.description
    if data.is_completed is not None:
        todo.is_completed = data.is_completed

    todo.save()
    return todo


def delete_todo(todo_id: int) -> None:
    todo = get_todo(todo_id)
    todo.delete()
