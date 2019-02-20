"""
arquivo: [ app.urls.py ]
autor: Saymon de Oliveira Souza ( saymon.souza@cogni.group )
propósito: rotas da app comuns da aplicação
data criação: 10/12/2018
última atualização: 10/11/2018

"""

from django.urls import path 
from django.views.decorators.csrf import csrf_exempt
from .views import index, card1, card2

urlpatterns = [
    path( '', index ),
    path( 'card1/', card1 ),
    path( 'card2/', card2 ),
]