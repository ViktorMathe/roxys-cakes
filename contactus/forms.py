from django.forms import ModelForm
from .models import Contact_us


class Contact_usForm(ModelForm):
    class Meta:
        model = Contact_us
        fields = '__all__'
