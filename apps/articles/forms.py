from django import forms
from .models import Article
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

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
            'author': forms.Select(
                attrs={'class':'form-control'}
            ),
            'categories': forms.CheckboxSelectMultiple()
        }