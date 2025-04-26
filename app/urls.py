from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("callback", views.callback, name="callback"),
    path("success", views.success, name="success"),
    path("logout", views.logout, name="logout"),
]