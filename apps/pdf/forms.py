from django import forms
from django.forms.widgets import ClearableFileInput

from apps.pdf.models import PDF_File, CSV_File


class UploadPDFForm(forms.ModelForm):
    class Meta:
        model = PDF_File
        fields = ['archivo']
        widgets = {
            'archivo': ClearableFileInput(attrs={'multiple': True})
        }


class UploadCSVForm(forms.ModelForm):
    class Meta:
        model = CSV_File
        fields = ['archivo']
