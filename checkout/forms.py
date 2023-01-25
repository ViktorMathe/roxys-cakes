from django import forms
from .models import Checkout


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ('full_name', 'email_address', 'phone_number',
                  'address_1', 'address_2',
                  'city', 'post_code', 'county',
                  'country',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'post_code': 'Postal Code',
            'city': 'Town or City',
            'address_1': 'Street Address 1',
            'address_2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
