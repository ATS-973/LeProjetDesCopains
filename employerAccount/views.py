from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CustomUser
from .forms import EmployerLoginForm
from django.shortcuts import get_object_or_404

def login(request):
    if request.method == 'POST':
        form = EmployerLoginForm
        if form.is_valid():
            return redirect('infosEmployer')
    else:
        form = EmployerLoginForm()
    return render(request, 'employer_login.html', {'form': form}) #A modifier pour bon fichier html