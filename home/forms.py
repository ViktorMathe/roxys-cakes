from django import forms
from .models import Subscribe, Newsletter
from django_summernote.widgets import SummernoteWidget


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email',)


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

        widgets = {
            'content': SummernoteWidget()
        }
