
from pyexpat.errors import messages
from django.shortcuts import render,get_object_or_404, redirect,reverse
from .models import articles
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Panier, articles, Commande
from django.contrib.auth.models import User
from django.contrib import messages


def Accueil(request):
    article =articles.objects.all()
    return render(request, 'index.html', {"article": article})
  
def about(request):
    return render(request, 'about.html')
  
def Nos_service(request):
    article = articles.objects.all().order_by('-id') 
    return render(request, 'service.html', {"article": article})
  
def Nos_contact(request):
    return render(request, 'contact.html')

@login_required(login_url="/login/")
def logout_user(request):
    logout(request)  
    return redirect('login')

@login_required(login_url="/login/")
def login(request):
    redirect('index') 
    return render(request, 'utilisateur/login.html') 
   
@login_required(login_url="/login/") 
def register_user(request):
    return render(request, 'utilisateur/register.html')

@login_required(login_url="/login/")
def details_articles(request, article_id):
    article = get_object_or_404(articles, id=article_id)  
    # url_panier = reverse('panier', kwargs={'article_id': article.id})  
    return render(request, 'article/details_articles.html', {'article': article})



  

