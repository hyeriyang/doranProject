from django import forms
from .models import Upload
# 윤아
class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['utitle', 'ubody', 'uvideo']