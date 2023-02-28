from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Tag, Task


def index(request):
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num tags": num_tags, "num_tasks": num_tasks,
    }
    return render(request, "catalog/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    template_name = "catalog/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("catalog:tag-list")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "catalog/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")

def toggle_to_done(request, pk):
    task = Task.objects.get(id=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse_lazy("catalog:task-list"))

