from typing import List
from .serializers import (
    TodoCreateRequestSerializer,
    TodoUpdateRequestSerializer,
    TodoPartialUpdateRequestSerializer,
)
from .dataclasses import TodoData, TodoUpdateData
from rest_framework.exceptions import ValidationError

# LIST / GET can remain simple helpers (no DB here by request)
# For read operations the view will call model/query directly or you can add a helper that returns querysets.

def prepare_create(request_data: dict) -> TodoData:
    """
    Controller -> calls serializer to validate request data.
    Returns a TodoData dataclass ready for the view to persist via model.
    """
    serializer = TodoCreateRequestSerializer(data=request_data)
    serializer.is_valid(raise_exception=True)
    v = serializer.validated_data
    return TodoData(
        title=v["title"],
        description=v.get("description", ""),
        is_completed=v.get("is_completed", False),
    )

def prepare_full_update(request_data: dict) -> TodoUpdateData:
    serializer = TodoUpdateRequestSerializer(data=request_data)
    serializer.is_valid(raise_exception=True)
    v = serializer.validated_data
    return TodoUpdateData(
        title=v["title"],
        description=v.get("description", ""),
        is_completed=v["is_completed"],
    )

def prepare_partial_update(request_data: dict) -> TodoUpdateData:
    serializer = TodoPartialUpdateRequestSerializer(data=request_data, partial=True)
    serializer.is_valid(raise_exception=True)
    v = serializer.validated_data
    return TodoUpdateData(
        title=v.get("title"),
        description=v.get("description"),
        is_completed=v.get("is_completed"),
    )
