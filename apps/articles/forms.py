from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'image',
            'author',
            'categories'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'content': forms.Textarea(
                attrs={'class':'form-control'}
            ),
            'author': forms.Select(
                attrs={'class':'form-control'}
            ),
            'categories': forms.CheckboxSelectMultiple()
        }