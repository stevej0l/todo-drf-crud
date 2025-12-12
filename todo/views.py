from typing import List
from .models import Todo
from .dataclasses import TodoData, TodoUpdateData

# READ
def list_todos_from_model() -> List[Todo]:
    return list(Todo.objects.all().order_by("-created_at"))

def get_todo_from_model(pk: int) -> Todo:
    return Todo.get_or_404(pk)

# CREATE
def create_todo_in_model(data: TodoData) -> Todo:
    # All DB create logic is inside the model
    return Todo.create_from_dataclass(data)

# UPDATE (both full + partial use same apply method)
def update_todo_in_model(pk: int, data: TodoUpdateData) -> Todo:
    todo = Todo.get_or_404(pk)
    return todo.apply_update_dataclass(data)

# DELETE
def delete_todo_in_model(pk: int) -> None:
    todo = Todo.get_or_404(pk)
    todo.delete()
