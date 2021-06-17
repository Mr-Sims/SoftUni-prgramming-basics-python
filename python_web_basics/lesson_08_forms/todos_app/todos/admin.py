from django.contrib import admin

# Register your models here.
from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Category, Person


# Option 2 - using decorator admin.register('app name here')
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['text', 'owner']
    sortable_by = ['text', ]
    list_filter = ['owner']

    # def has_change_permission(self, request, obj=None):
    #     return False

# Option 1 - using command admin.site.register('app name here')
# admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)