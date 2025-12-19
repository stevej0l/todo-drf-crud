from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create_todo(data):
        return Todo.objects.create(**data)

    @staticmethod
    def list_todos():
        return Todo.objects.all().order_by("-created_at")

    def update_todo(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.save()
        return self

    def delete_todo(self):
        self.delete()
