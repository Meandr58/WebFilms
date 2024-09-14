from django import forms
from .models import Films_post
from django.forms import ModelForm, TextInput, DateInput, Textarea

class Films_postForm(ModelForm):
    class Meta:
        model = Films_post
        fields = ['title', 'text1', 'text2', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'text1': Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое содержание'}),
            'text2': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв о фильме'}),
            'pub_date': DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации', 'type': 'date'})
        }
