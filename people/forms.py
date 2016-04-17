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
        password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
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

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long.")

        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            exists = User.objects.get(email=email)
            raise forms.ValidationError("This email is already in use.")
        except User.DoesNotExist:
            return email
