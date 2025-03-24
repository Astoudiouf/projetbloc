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
  login,
  logout_user,
  register_user,

)


urlpatterns = [
  path('', Accueil, name='index'),
  path('about/', about, name='about'),
  path('service/', Nos_service, name='service'),
  path('contact/', Nos_contact, name='contact'),
  path('details_articles/<int:article_id>/', details_articles, name='details_articles'),
  path('login/',login,name="login"),
  path('logout/',logout_user,name="logout"),
  path('register/',register_user,name="register"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)