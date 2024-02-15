from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("user/<int:user_id>/", views.infos, name="infosUser"),
    path("user/login/", views.login, name="userLogin"),
]