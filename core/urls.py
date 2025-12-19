from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.feature.todo.urls")),  # <--- this is the entry point for our flow
]
