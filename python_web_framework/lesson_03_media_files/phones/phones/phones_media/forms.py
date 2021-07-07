from django import forms

from phones.phones_media.models import Phone, PhoneImages


class PhoneForm(forms.ModelForm):
    image = forms.ImageField()

    def save(self, commit=True):
        phone = super().save(commit=commit)

        phone_image = PhoneImages(
            image=self.cleaned_data['image'],
            phone=phone,
            is_selected=True
        )
        if commit:
            phone_image.save()

        return phone


    class Meta:
        model = Phone
        fields = '__all__'
