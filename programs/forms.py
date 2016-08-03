from django import forms
from .models import Programs


class AddProgramForm(forms.ModelForm):
    class Meta:
        model = Programs
        fields = ('name', 'location', 'description', 'slug', 'details', 'start_date', 'end_date', 'fee',
                  'phone_contact', 'email_contact', 'deadline', 'picture')
        slug = forms.SlugField(label='slug')
        fee = forms.IntegerField()
        picture = forms.ImageField()
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name of the Program',
                    'required': True,
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Where it will take place/be offered',
                    'required': True,
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Description',
                    'required': True,
                }
            ),
            'details': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Other Details about the Program',
                    'required': True,
                }
            ),
            'start_date': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Start Date',
                    'required': True,
                }
            ),
            'end_date': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'End Date',
                    'required': True,
                }
            ),
            'phone_contact': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contact by Phone',
                    'required': True,
                }
            ),
            'email_contact': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contact by Email',
                    'required': True,
                }
            ),
            'deadline': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Deadline to apply for the Program',
                    'required': True,
                }
            ),
        }