from django.contrib import admin

from recipes.recipes_app.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title',]


admin.site.register(Recipe, RecipeAdmin)
