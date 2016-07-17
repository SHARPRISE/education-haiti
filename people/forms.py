from django import forms

from people.models import User
from people.models import UNIVERSITIES, Mentor
# Create your forms here.

"""class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

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
        }"""

class MentorLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'undergrad_college')
        undergrad_college = forms.MultipleChoiceField(
            choices=UNIVERSITIES,
            label='Choose your university',
            initial='',
            widget=forms.SelectMultiple(),
            required=True
        )
        widgets = {
            'username' : forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'username',
                    'required': True,
                }
            ),
            'password': forms.PasswordInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'password',
                    'required': True,
                }
            )
        }


"""class RegisterForm(forms.ModelForm):
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
                    'required' : False,
                    'placeholder' : "Mentor or mentee"
                },
            )
        }"""
class MentorUpdateForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('biography','grad_college','majors','interests','residency','phone','current_status','school_haiti','first_name',
                  'last_name','picture')
        biography = forms.TextInput()
        grad_college = forms.MultipleChoiceField(
            choices=UNIVERSITIES,
            label='Choose your Graduate College',
            initial='',
            widget=forms.SelectMultiple(),
            required=True
        )
        majors = forms.CharField(label="Seperate each major with a comma, ex: Electrical Engineering, Economy")
        interests = forms.CharField(label="Separate each interest with a comma, ex: Education, Computer Science")
        residency = forms.CharField()
        phone = forms.CharField()
        current_status = forms.CharField(label='Your current status, ex: Analyst, CEO, etc')
        school_haiti = forms.CharField(label='Your High School back in Haiti')
        first_name = forms.CharField(label='Your First and Middle Name(s)')
        last_name = forms.CharField(label='Your Last Name')
        picture = forms.ImageField(label='Upload your profile picture')

class MentorRegisterForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ('email', 'username', 'password', 'undergrad_college')
        password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
        undergrad_college = forms.MultipleChoiceField(
            choices=UNIVERSITIES,
            label = 'Choose your university',
            initial = '',
            widget = forms.SelectMultiple(),
            required = True
                                    )
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
