from django.urls import path
from . import views

urlpatterns = [
    path("employer/<int:employer_id>", views.infos, name="infosEmployer"),
]