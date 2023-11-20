from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect()  # Inclure le nom de la page WEB accueil
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form}) # Modifier pour pointer vers la page de création de compte