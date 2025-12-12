from django.db import models
from dataclasses import asdict
from .dataclasses import TodoData, TodoUpdateData

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @classmethod
    def create_from_dataclass(cls, data: TodoData) -> "Todo":
        kwargs = asdict(data)
        return cls.objects.create(**kwargs)

    def apply_update_dataclass(self, data: TodoUpdateData) -> "Todo":
        if data.title is not None:
            self.title = data.title
        if data.description is not None:
            self.description = data.description
        if data.is_completed is not None:
            self.is_completed = data.is_completed
        self.save()
        return self

    @classmethod
    def get_or_404(cls, pk: int):
        from django.shortcuts import get_object_or_404
        return get_object_or_404(cls, id=pk)
