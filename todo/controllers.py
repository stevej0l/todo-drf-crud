from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    TodoCreateRequestSerializer,
    TodoUpdateRequestSerializer,
    TodoPartialUpdateRequestSerializer,
    TodoResponseSerializer,
)
from .dataclasses import TodoData, TodoUpdateData
# controllers import helper functions from views.py
from . import views as todo_views


@api_view(["GET", "POST"])
def todo_list_create(request):
    """
    Controller endpoint:
    - validates request
    - converts to dataclass
    - calls view-layer function which interacts with model
    """
    if request.method == "GET":
        todos = todo_views.list_todos_from_model()
        return Response(TodoResponseSerializer(todos, many=True).data)

    # POST -> validate using request serializer
    req_ser = TodoCreateRequestSerializer(data=request.data)
    req_ser.is_valid(raise_exception=True)
    v = req_ser.validated_data

    # convert to dataclass
    todo_dc = TodoData(
        title=v["title"],
        description=v.get("description", ""),
        is_completed=v.get("is_completed", False),
    )

    # call view-layer function to persist (model-level create happens inside models.py)
    todo = todo_views.create_todo_in_model(todo_dc)
    return Response(TodoResponseSerializer(todo).data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def todo_detail(request, pk: int):
    if request.method == "GET":
        todo = todo_views.get_todo_from_model(pk)
        return Response(TodoResponseSerializer(todo).data)

    if request.method == "DELETE":
        todo_views.delete_todo_in_model(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "PUT":
        req_ser = TodoUpdateRequestSerializer(data=request.data)
        req_ser.is_valid(raise_exception=True)
        v = req_ser.validated_data
        update_dc = TodoUpdateData(
            title=v["title"],
            description=v.get("description", ""),
            is_completed=v["is_completed"],
        )
        updated = todo_views.update_todo_in_model(pk, update_dc)
        return Response(TodoResponseSerializer(updated).data)

    if request.method == "PATCH":
        req_ser = TodoPartialUpdateRequestSerializer(data=request.data, partial=True)
        req_ser.is_valid(raise_exception=True)
        v = req_ser.validated_data
        update_dc = TodoUpdateData(
            title=v.get("title"),
            description=v.get("description"),
            is_completed=v.get("is_completed"),
        )
        updated = todo_views.update_todo_in_model(pk, update_dc)
        return Response(TodoResponseSerializer(updated).data)
