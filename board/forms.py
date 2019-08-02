from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['subject','memo']
        widgets = {
            'subject':forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'cols': 100}),
            'memo': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'cols': 100})
            }
        labels = {'subject':'제목', 'memo':'내용'}      


class BoardCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_textfield']
        widgets = {
            'comment_textfield': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'cols': 40})
            }
        labels = {'comment_textfield':''}