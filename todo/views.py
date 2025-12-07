from dataclasses import asdict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import controllers
from .dataclasses import TodoData, TodoUpdateData
from .serializers import TodoSerializer


class TodoListCreateView(APIView):
    """
    GET  /api/todos/      -> list all todos
    POST /api/todos/      -> create new todo
    """

    def get(self, request):
        todos = controllers.list_todos()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Convert validated data into dataclass, call controller
        data = TodoData(**serializer.validated_data)
        todo = controllers.create_todo(data)
        out_serializer = TodoSerializer(todo)
        return Response(out_serializer.data, status=status.HTTP_201_CREATED)


class TodoDetailView(APIView):
    """
    GET    /api/todos/<id>/   -> retrieve one
    PUT    /api/todos/<id>/   -> full update
    PATCH  /api/todos/<id>/   -> partial update
    DELETE /api/todos/<id>/   -> delete
    """

    def get(self, request, pk: int):
        todo = controllers.get_todo(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk: int):
        todo = controllers.get_todo(pk)
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)

        data = TodoUpdateData(**serializer.validated_data)
        updated_todo = controllers.update_todo(pk, data)
        out_serializer = TodoSerializer(updated_todo)
        return Response(out_serializer.data)

    def patch(self, request, pk: int):
        todo = controllers.get_todo(pk)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        data = TodoUpdateData(**serializer.validated_data)
        updated_todo = controllers.update_todo(pk, data)
        out_serializer = TodoSerializer(updated_todo)
        return Response(out_serializer.data)

    def delete(self, request, pk: int):
        controllers.delete_todo(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
