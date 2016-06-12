from django.contrib import admin

# Register your models here.
from apps.pdf.models import PDF_File, CSV_File, Visualizar

admin.site.register(PDF_File)
admin.site.register(CSV_File)
admin.site.register(Visualizar)