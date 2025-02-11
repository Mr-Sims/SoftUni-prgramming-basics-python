from django.db import models

from todos_app.todos.validators import validate_dot


class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural='People'


class Category(models.Model):
    HOME_CHOICE = 'Home'
    WORK_CHOICE = 'Work'
    NAME_CHOICES = (
        (HOME_CHOICE, 'Home stuff'),
        (WORK_CHOICE, 'Work stuff')
    )

    name = models.CharField(
        max_length=20,
        choices= NAME_CHOICES
    )

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name_plural="Categories "


class Todo(models.Model):
    text = models.CharField(
        max_length=30,
        validators=(validate_dot,)
    )
    state = models.BooleanField(
        default=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True,
        blank=True,

    )
    categories = models.ManyToManyField(Category)

    # def __str__(self):
    #     return f"{self.text}"