from django import forms

from people.models import User
# Create your forms here.

class LoginForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ('username', 'password',)
        widgets = {
            'username' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'username',
                    'required' : True,
                }
            ),
            'password' : forms.PasswordInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'password',
                    'required' : True,
                }
            )
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ('email', 'username', 'password', 'rank')
        widgets = {
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'email',
                    'required' : True,
                }
            ),
            'username' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'username',
                    'required' : True,
                }
            ),
            'password' : forms.PasswordInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'password',
                    'required' : True,
                }
            ),
            'rank'     : forms.RadioSelect(
                attrs = {
                    'class' : 'form-control',
                    'required' : True,
                    'placeholder' : "Mentor or mentee"
                },
            )
        }
