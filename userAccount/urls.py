from django.contrib import admin
from django.urls import path
from userAccount import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'), # A modifier pour pointer vers la page de création de compte 
]