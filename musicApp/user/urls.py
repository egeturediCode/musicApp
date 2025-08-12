from django.urls import path
from . import views
#http://127.0.0.1:8000/register            =>register


urlpatterns = [
    path("user/register",  views.Register),
    path("user/login", views.Login),
    path("user/logout", views.Logout)

]