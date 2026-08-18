from django.contrib import admin

from todo.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "created_at",
        "deadline",
        "is_done",
    )
    list_filter = ("is_done", "tags")
    search_fields = ("content",)
    filter_horizontal = ("tags",)
