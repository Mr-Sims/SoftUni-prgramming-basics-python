from django.db import models


class Phone(models.Model):
    manufacturer = models.CharField(
        max_length=30,
    )
    model = models.CharField(
        max_length=15,
    )

    def __str__(self):
        return f'{self.manufacturer} - {self.model}'


class PhoneImages(models.Model):
    image = models.ImageField(
        upload_to='phones',
    )
    is_selected = models.BooleanField(
        default=False,
    )
    phone = models.ForeignKey(
        Phone,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.phone.manufacturer} - {self.phone.model}'


##Initial model was&
# class Phone(models.Model):
#     manufacturer = models.CharField(
#         max_length=30,
#     )
#     model = models.CharField(
#         max_length=15,
#     )
#     image = models.ImageField(
#         upload_to='phones',
#         blank=True,
#     )
