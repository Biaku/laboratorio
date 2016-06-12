from django.conf.urls import url

from apps.pdf.views import cpanel, guardar_csv, guardar_pdf, mostrar_resultados

urlpatterns = [
    url(r'^cpanel/', cpanel, name='cpanel'),
    url(r'^guardar_csv/', guardar_csv, name='guardar_csv'),
    url(r'^guardar_pdfs/', guardar_pdf, name='guardar_pdfs'),
    url(r'^resultados/', mostrar_resultados, name='resultados'),
]
