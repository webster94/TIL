from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '수정된 아티틀 라벨',
        widget = forms.TextInput(attrs={
            'class' : 'form-control'
        })
    )
    
    class Meta:
        model = Article
        fields = "__all__"
