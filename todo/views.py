from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag

class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"

class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    template_name = "todo/form.html"
    success_url = reverse_lazy("task-list")

class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    template_name = "todo/form.html"
    success_url = reverse_lazy("task-list")

class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("task-list")

class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"

class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/form.html"
    success_url = reverse_lazy("tag-list")

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "todo/form.html"
    success_url = reverse_lazy("tag-list")

class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("tag-list")

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("task-list")
