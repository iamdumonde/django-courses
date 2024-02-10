from django.db import models

# Create your models here.
#Livre
class Livre(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255)
    auteur = models.ForeignKey("Auteur", on_delete=models.CASCADE)
    description = models.TextField(help_text='Ajouter un bref résumé du livre')
    image = models.ImageField(upload_to='images/', help_text="Ajouter une image", blank=True, null=True)
    categorie = models.ManyToManyField("Categorie", help_text='Choisissez la catégorie du livre')
    en_stock = models.BooleanField(default=True)
    date_d_ajout = models.DateField(auto_now_add=True)
    date_publication = models.DateField(help_text='Entrer la date de la publication')
    date_update = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.titre
    

#Auteur
class Auteur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="authorsImage", help_text="Ajouter l'image de l'auteur", blank=True, null=True)
    biographie = models.TextField()
    
    def __str__(self) -> str:
        return self.nom
    
#Catégorie
class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.description
    
