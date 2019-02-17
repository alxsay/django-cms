"""
arquivo: [ app.urls.py ]
autor: Saymon de Oliveira Souza ( saymon.souza@cogni.group )
propósito: rotas da app comuns da aplicação
data criação: 10/12/2018
última atualização: 10/11/2018

"""

from django.urls import path 
from django.views.decorators.csrf import csrf_exempt
from .views import index

urlpatterns = [
    #path( '', AppView.as_view( template_name = 'index.html' ) ),
    path( '', index ),
]