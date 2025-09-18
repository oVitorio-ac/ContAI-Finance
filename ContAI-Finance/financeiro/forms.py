from django import forms
from .models import UploadArquivo


class UploadArquivoForm(forms.ModelForm):
    """
    Form for uploading files.
    """
    class Meta:
        model = UploadArquivo
        fields = ['titulo', 'arquivo']