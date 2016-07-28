from django import forms

from .models import SuccessStory


class AddStoryForm(forms.ModelForm):
    class Meta:
        model = SuccessStory
        fields = ('title', 'slug','description', 'content','published','article_picture')
        slug = forms.SlugField(label='slug')
        published = forms.CheckboxInput()
        article_picture = forms.ImageField()
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Title',
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
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Text Content',
                    'required': True,
                }
            ),
        }
