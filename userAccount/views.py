from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CustomUser

def infos(request, user_id):
    user = CustomUser.objects.filter(user_id=user_id)
    template = loader.get_template("user.html")
    context = {user: "user"}

    return HttpResponse(template.render(context, request))
