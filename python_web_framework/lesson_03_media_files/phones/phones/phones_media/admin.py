from django.contrib import admin

from phones.phones_media.models import Phone, PhoneImages


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneImages)
class PhoneImageAdmin(admin.ModelAdmin):
    pass