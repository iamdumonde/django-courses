from django.urls import path
from . import views
from .views import DetailLivre, ListeLivre, Ma_vue, ListeAuteurs

urlpatterns = [
    path('index/', views.my_vue, name='index'),
    path('maClassvue/', Ma_vue.as_view(), name='maClassvue'),#same
    path('maClassvue/', views.Ma_vue.get, name='maClassvue'),#same
    path('livredetails/<int:id>/', DetailLivre.as_view(), name='livredetails'),
    path('allLivres/', ListeLivre.as_view(), name='allLivres'),
    path('', ListeLivre.as_view(), name='allLivres'),
    path('liste_auteur', ListeAuteurs.as_view(), name='liste_auteur'),
]
