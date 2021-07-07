from django.shortcuts import render, redirect

from phones.phones_media.forms import PhoneForm
from phones.phones_media.models import Phone


def index(request):
    phones = Phone.objects.all()
    for phone in phones:
        phone.selected_image = phone.phoneimages_set.filter(is_selected=True).first()
        pass
    form = PhoneForm()
    context = {
        'phones': phones,
        'form': form
    }
    return render(request, 'index.html', context)


def create_phone(request):
    form = PhoneForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')

