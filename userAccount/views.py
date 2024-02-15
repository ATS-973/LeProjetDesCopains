from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CustomUser
from .forms import UserLoginForm
from django.shortcuts import get_object_or_404

def infos(request, user_id):
    user = user = get_object_or_404(CustomUser, user_id=user_id)
    template = loader.get_template("user.html")
    context = {"user": user}

    return HttpResponse(template.render(context, request))

def login(request):
    if request.method == 'POST':
        form = UserLoginForm
        if form.is_valid():
            return redirect('infosUser')
    else:
        form = PersonalLoginForm()
    return render(request, 'personal_login.html', {'form': form}) #A modifier pour bon fichier html
