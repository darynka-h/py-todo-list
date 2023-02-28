from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import Tag, Task, Executor


@admin.register(Executor)
class ExecutorAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("task_tag",)


admin.site.register(Tag)
