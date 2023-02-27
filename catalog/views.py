from django.shortcuts import render

from catalog.models import Tag, Task


def index(request):
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num tags": num_tags, "num_tasks": num_tasks,
    }
    return render(request, "catalog/index.html", context=context)