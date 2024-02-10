from typing import Any, Dict, Optional
from django.db.models.query import QuerySet
from django.db.models.base import Model as Model
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import (DetailView, ListView)
from .models import *

# Create your views here.

def my_vue(request):
    contenue = "It is the best moment to learn life"
    return HttpResponse(contenue)

class Ma_vue(View):
    def get(self, request):
        contenue = "In my class Ma_vue"
        return HttpResponse(contenue)



class DetailLivre(DetailView):
    model = 'Livre'
    template_name = 'livre_detail.html'
    context_object_name = 'livre'
    
    def get_object(self, queryset = None):
        return (Livre.objects.get(pk=self.kwargs['id']))
    
    
class ListeLivre(ListView):
    model = 'Livre'
    template_name = 'livre_list.html'
    context_object_name = 'les_livres'
    
    def get_queryset(self):
        #récupérer les livres à afficher
        return Livre.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class ListeAuteurs(ListView):
    model = 'Auteur'
    template_name = 'auteurs_list.html'
    context_object_name = 'les_auteurs'
    
    def  get_queryset(self):
        qs = Auteur.objects.all().order_by('nom')  
        return qs
    
    def  get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
    
    
class DetailAuteur(DetailView):
    model = 'Auteur'
    template_name = 'auteur_detail.html'
    context_object_name = 'auteur'
    
    def get_object(self, queryset = None):
        return (Auteur.objects.get(pk=self.kwargs['id']))
    
