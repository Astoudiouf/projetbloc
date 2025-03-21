
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
    url_panier = reverse('panier', kwargs={'article_id': article.id})  

    return render(request, 'article/details_articles.html', {'article': article, 'url_panier': url_panier})

@login_required(login_url="/login/")
def new_articles(request):
    if request.method == "POST":
        titre = request.POST.get('titre')  
        prix = request.POST.get('prix')

        if titre and prix:  
            Article = articles.objects.create(
                titre=titre,
                prix=prix,  
            )
            Article.save()
            return redirect("index")  
        else:
            return render(request, 'article/new_articles.html', {"error": "Tous les champs sont obligatoires"})

    return render(request, 'article/new_articles.html')


@login_required(login_url="/login/")
def update_articles(request, id):
    article = get_object_or_404(articles, id=id)
    if request.method == "POST":
        titre = request.POST.get('titre', article.titre)
        contenu = request.POST.get('contenu', article.Contenu)
        Article_to_update=article.objects.filter(pk=article.id)
        Article_to_update.update(
            titre=titre,
            Contenu=contenu,
        )
        article.save()

        return redirect("/index/") 
    return render(request, "article/update_article.html", {"article": article})

# @login_required(login_url="/login/")
# def afficher_panier(request):
#     panier = Panier.objects.filter(user=request.user) 
#     total = sum(item.total() for item in panier)
#     return render(request, 'panier/panier.html', {'panier': panier, 'total': total})
  

@login_required(login_url="/login/")
def delete_article(request, panier_id):
    article = get_object_or_404(Panier, id=panier_id, user=request.user)
    article.delete()
    return redirect('afficher_panier')

# @login_required(login_url="/login/")
# def afficher_panier(request, article_id):
#     Article = get_object_or_404(articles, id=article_id)
#     panier = Panier.objects.filter(user=request.user, Article=Article).first()
#     if panier:
#         panier.quantite += 1
#         panier.save()
#     else:
#         Panier.objects.create(user=request.user, Article=Article)
#     return redirect('panier')





def ajouter_au_panier(request, article_id):
    article = get_object_or_404(articles, id=article_id)
    panier, created = Panier.objects.get_or_create(user=request.user)  
    panier.articles.add(article)  
    return redirect(reverse('panier'))


@login_required(login_url="/login/") 
def voir_panier(request):
    if request.user.is_authenticated:
     article= Panier.objects.all() 
     return render(request, 'panier/panier.html', {'article': article})



@login_required(login_url="/login/")
def supprimer_du_panier(request, article_id):
    item = get_object_or_404(Panier, articles_id=article_id, user=request.user)  
    item.delete()

    return redirect('voir_panier')  



def passer_commande(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        total = request.POST.get('total')

        if nom and total:  
            Commande.objects.create(nom=nom, total=total)
            return redirect('liste_commandes') 
    
    return render(request, 'commande/commande.html')


def liste_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'commande/commande.html', {'commandes': commandes})

