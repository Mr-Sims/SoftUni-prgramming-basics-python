from django.contrib import admin

from templates_advanced_demo.todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['text']