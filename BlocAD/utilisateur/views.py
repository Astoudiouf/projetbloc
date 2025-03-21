from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")  # Assurez-vous que 'index' est bien défini dans urls.py
            else:
                messages.error(request, "Email ou mot de passe incorrect.")

    return render(request, "utilisateur/login.html", {"form": form})

def login(request):
    return render(request, "login.html")

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST) 
        if form.is_valid():
            user = form.save()  
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=raw_password)
            return redirect("/login/")
        else:
            print(form.errors)  
    else:
        form = SignUpForm()

    return render(request, "utilisateur/register.html", {"form": form})
  
