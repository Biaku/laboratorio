from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.

def iniciar_sesion(request):
    mensaje = None
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if username == 'pagaduria':
                    return redirect('actividades', estatus='activas')
                else:
                    return redirect('dashboard')
            else:
                mensaje = 'Cuenta desactivada'
                return render(request, 'login.html', {'msj': mensaje})
        else:
            mensaje = 'Credenciales incorrectas'
    return render(request, 'login.html', {'msj': mensaje})


def desconectar(request):
    logout(request)
    return redirect('inicio-sesion')
