from .views import login_view, register_user, login
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/',login_view,name="login"),
    path('register/',register_user,name="register"),
    path('login/',login,name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
]
