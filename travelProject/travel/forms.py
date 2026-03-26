from django import forms
from .models import Review

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'body']  # 입력받을 필드를 정의