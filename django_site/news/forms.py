from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title news'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons news'
            }),
            'title': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text news'
            }),
            'title': DateTimeInput(attrs={
                'class': 'form-control'
            }),
        }
