from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['subject','memo']     


class BoardCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_textfield']
        widgets = {
            'comment_textfield': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'cols': 40})
            }
        labels = {'comment_textfield':''}