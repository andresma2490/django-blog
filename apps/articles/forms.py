from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Article

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = [
            'title',
            'resume',
            'content',
            'image',
            'categories',
            'keywords'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'categories': forms.CheckboxSelectMultiple()
        }