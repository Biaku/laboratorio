from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv
from apps.pdf.forms import UploadPDFForm, UploadCSVForm
from apps.pdf.models import PDF_File, CSV_File, Visualizar
from PyPDF2 import PdfFileReader, PdfFileWriter


def cpanel(request):
    form_pdf = UploadPDFForm()
    form_csv = UploadCSVForm()
    variables = {
        'form_pdf': form_pdf,
        'form_csv': form_csv,
    }
    return render(request, 'pdf/cpanel.html', variables)


def guardar_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file = CSV_File.objects.latest('id')
            with open('media/' + file.archivo.__str__(), newline='') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    try:  # cuando el usuario ya exista
                        usuario = User.objects.get(username=row[0])
                        registro = Visualizar()
                        registro.usuario = usuario
                        registro.ruta_pdf = 'pdf/' + row[3]
                        registro.save()
                    except User.DoesNotExist:  # cuando el usuario aun no exista
                        # crear el usuario
                        usuario = User()
                        usuario.username = row[0]
                        usuario.password = row[1]
                        usuario.first_name = row[2]
                        # agregar los permisos para el usuario

                        usuario.save()
                        # obtiene el ultimo usuario registrado
                        nuevo_usuario = User.objects.latest('id')
                        # inserta los datos para que se pueda visualizar los pdf
                        registro = Visualizar()
                        registro.usuario = nuevo_usuario
                        registro.ruta_pdf = 'media/pdf/' + row[3]
                        registro.save()
            return redirect(reverse('pdf:cpanel'))
        else:
            return HttpResponse(form.errors)


def guardar_pdf(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        files = request.FILES.getlist('archivo')
        if form.is_valid():

            for archivo in files:
                pdf = PDF_File()
                pdf.archivo = archivo
                pdf.save()
            return redirect(reverse('pdf:cpanel'))
        else:
            print(form.errors)


def mostrar_resultados(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="resultados.pdf"'

    resultados = Visualizar.objects.all().filter(usuario_id=6)

    pdf = PdfFileWriter()

    for item in resultados:
        pagina = PdfFileReader(open('media/'+item.ruta_pdf + '.pdf', 'rb'))
        pdf.addPage(pagina.getPage(0))
    pdf.write(response)
    return response
