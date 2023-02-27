from django.urls import path

from catalog.views import index, TagListView, TaskListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list",
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),
]


app_name = "catalog"