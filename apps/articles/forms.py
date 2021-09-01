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
            'resume': forms.Textarea(
                attrs={'class':'form-control', 'rows':5 }
            ),
            'keywords': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'categories': forms.CheckboxSelectMultiple()
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) >= 100:
            self.add_error("title", "value too long for title (max 100 characters)")
        return title
