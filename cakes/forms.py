from django import forms
from .models import Cake


class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
