from django.db import models
from django.contrib.auth.models import User

class articles(models.Model):
  titre=models.CharField(max_length=150)
  Resume=models.CharField(max_length=150)
  auteur=models.CharField(max_length=150,null=True,blank=True)
  Contenu=models.CharField(max_length=150)
  Date_de_mise_a_jour=models.DateTimeField(auto_now_add=True)
  disponible = models.BooleanField(default=True)
  prix=models.FloatField()
  image=models.ImageField(upload_to='images/',null=True,blank=True)
  
  def __str__(self):
      return f"{self.titre} {self.Contenu} {self.disponible} {self.prix}"
  

class Panier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    articles = models.ForeignKey(articles, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite}x {self.articles}€"
    
    
    
class Commande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Commande {self.id} de {self.user.username}"
