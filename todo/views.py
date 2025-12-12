from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import controllers
from .models import Todo
from .serializers import TodoResponseSerializer
from .dataclasses import TodoData, TodoUpdateData

@api_view(["GET", "POST"])
def todo_list_create(request):
    if request.method == "GET":
        qs = Todo.objects.all().order_by("-created_at")
        return Response(TodoResponseSerializer(qs, many=True).data)

    # POST: controller -> serializer validation -> returns TodoData dataclass
    todo_dc: TodoData = controllers.prepare_create(request.data)

    # View now invokes the model-level create function (DB call lives in models.py)
    todo = Todo.create_from_dataclass(todo_dc)

    return Response(TodoResponseSerializer(todo).data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def todo_detail(request, pk):
    # GET
    if request.method == "GET":
        todo = Todo.get_or_404(pk)
        return Response(TodoResponseSerializer(todo).data)

    # DELETE
    if request.method == "DELETE":
        todo = Todo.get_or_404(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # PUT (full update)
    if request.method == "PUT":
        update_dc: TodoUpdateData = controllers.prepare_full_update(request.data)
        todo = Todo.get_or_404(pk)
        updated = todo.apply_update_dataclass(update_dc)  # persists inside model
        return Response(TodoResponseSerializer(updated).data)

    # PATCH (partial)
    if request.method == "PATCH":
        update_dc: TodoUpdateData = controllers.prepare_partial_update(request.data)
        todo = Todo.get_or_404(pk)
        updated = todo.apply_update_dataclass(update_dc)  # persists inside model
        return Response(TodoResponseSerializer(updated).data)
