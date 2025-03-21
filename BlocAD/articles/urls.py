from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
  Accueil,
  about, 
  Nos_service, 
  Nos_contact, 
  details_articles, 
  new_articles,
  update_articles,
  delete_article,
  login,
  logout_user,
  register_user,
  voir_panier,
  ajouter_au_panier,
  supprimer_du_panier,
  passer_commande,
  liste_commandes
)


urlpatterns = [
  path('', Accueil, name='index'),
  path('about/', about, name='about'),
  path('service/', Nos_service, name='service'),
  path('contact/', Nos_contact, name='contact'),
  path('details_articles/<int:article_id>/', details_articles, name='details_articles'),
  path('new_articles/', new_articles, name='new_articles'),
  path('update_articles/<int:id>/', update_articles, name='update_articles'),
  # path('afficher_panier/', afficher_panier, name='afficher_panier'),
  path('delete_article/<int:id>/', delete_article, name='delete_article'),
  path('panier/', voir_panier, name='panier'),
  path('ajouter_panier/<int:article_id>/', ajouter_au_panier, name='ajouter_panier'),
  path('login/',login,name="login"),
  path('logout/',logout_user,name="logout"),
  path('register/',register_user,name="register"),
  path('supprimer_du_panier/<int:article_id>/', supprimer_du_panier, name='supprimer_du_panier'),
  path('passer_commande/', passer_commande, name='passer_commande'),
  path('commandes/', liste_commandes, name='liste_commandes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)