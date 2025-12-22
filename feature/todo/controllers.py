from rest_framework.decorators import api_view
from rest_framework import status

from .serializers.request_serializers import TodoRequestSerializer
from .serializers.response_serializers import TodoResponseSerializer
from .services import (
    list_todos_paginated,
    create_todo,
    update_todo,
    delete_todo
)
from .models import Todo
from core.feature.common.utils import success_response, error_response


@api_view(["POST"])
def create_todo_controller(request):
    serializer = TodoRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return error_response(
            message="Validation failed",
            errors=serializer.errors
        )

    todo = create_todo(serializer.validated_data)

    return success_response(
        message="Todo created successfully",
        data=TodoResponseSerializer(todo).data,
        status_code=status.HTTP_201_CREATED
    )


@api_view(["GET"])
def list_todos_controller(request):
    page = int(request.query_params.get("page", 1))
    page_size = int(request.query_params.get("page_size", 10))

    result = list_todos_paginated(page, page_size)

    return success_response(
        message="Data fetched successfully",
        data=TodoResponseSerializer(result["items"], many=True).data,
        pagination=result["pagination"]
    )


@api_view(["GET"])
def get_todo_controller(request):
    todo_id = request.query_params.get("id")
    if not todo_id:
        return error_response(message="id is required")

    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return error_response(
            message="Todo not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return success_response(
        message="Data fetched successfully",
        data=TodoResponseSerializer(todo).data
    )


@api_view(["PUT"])
def update_todo_controller(request):
    todo_id = request.query_params.get("id")
    if not todo_id:
        return error_response(message="id is required")

    serializer = TodoRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return error_response(
            message="Validation failed",
            errors=serializer.errors
        )

    todo = update_todo(todo_id, serializer.validated_data)

    return success_response(
        message="Todo updated successfully",
        data=TodoResponseSerializer(todo).data
    )


@api_view(["DELETE"])
def delete_todo_controller(request):
    todo_id = request.query_params.get("id")
    if not todo_id:
        return error_response(message="id is required")

    delete_todo(todo_id)

    return success_response(
        message="Todo deleted successfully"
    )
