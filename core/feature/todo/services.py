from django.core.paginator import Paginator
from .models import Todo
from ..common.constants import DEFAULT_PAGE_SIZE


def list_todos_paginated(page: int, page_size: int = DEFAULT_PAGE_SIZE):
    queryset = Todo.objects.all().order_by("-created_at")
    paginator = Paginator(queryset, page_size)
    page_obj = paginator.get_page(page)

    return {
        "items": page_obj.object_list,
        "pagination": {
            "page": page_obj.number,
            "page_size": page_size,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        }
    }


def create_todo(todo_data: dict):
    return Todo.objects.create(**todo_data)


def update_todo(todo_id: int, todo_data: dict):
    todo = Todo.objects.get(id=todo_id)
    for key, value in todo_data.items():
        setattr(todo, key, value)
    todo.save()
    return todo


def delete_todo(todo_id: int):
    Todo.objects.get(id=todo_id).delete()
