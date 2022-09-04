from .models import Address
from django import forms
#from vi_address.models import City



class AddressForm(forms.ModelForm):
    class Meta:
        model = Address        
        fields = [
            'city',
            'district',
            'ward',
            'street',
            'building',
            'house_no',                          
        ]
        widgets = {
            'city': forms.Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }
            ),
            'district': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',
                }
            ), 
            'ward': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',
                }
            ),
            'street': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',
                }
            ),
            'building': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',
                }
            ),
            'house_no': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }
            ),            
        }
