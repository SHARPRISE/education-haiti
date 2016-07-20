from django import forms

from .models import SuccessStory


class AddStoryForm(forms.ModelForm):
    class Meta:
        model = SuccessStory
        fields = ('title', 'slug','description', 'content','published','article_picture')
        title = forms.CharField(label='Title')
        slug = forms.SlugField(label='slug')
        description = forms.CharField(label="Article's description")
        content = forms.TextInput()
        published = forms.CheckboxInput()
        article_picture = forms.ImageField()
