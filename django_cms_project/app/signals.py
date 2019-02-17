"""
arquivo: app.signals.py
autor: Saymon de Oliveira Souza ( saymon.souza@cogni.group )
propósito: Gatilhos para informar o monitor, via websocket, que alterações no banco de dados do microservice
ocorreram

OBS:

1 - possíveis mudanças no microservice:

    1 - inserir, editar, excluir:
        - empresa, planta, setor, medição setorial, unidade consumidora, ponto de medição, configuração de alerta


@receiver( post_save, sender = PontoDeMedicao )
def insert_resume_register_after_ponto_de_medicao( sender, instance, created, **kwargs ):
    pass

    - insert_resume_register_after_ponto_de_medicao é a handler function.
    - o decorator @receiver possui dois parâmetros, o primeiro, post_save é o signal, o segundo, trata-se do modelo que emitiu o evento
    - parâmetros da handling function:
        - sender -> classe modelo que disparou o envento
        - instance -> instância da classe salva
        - created -> valor booleano para indicar que a instância da classe modelo fora criada

"""

from django.forms.models import model_to_dict
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

import json

# informa mudanças relativas a EMPRESA
@receiver( post_save, sender = None )
def test_signals( sender, instance, created, **kwargs ):
    #if created:
    print( "Signal funcionando" )
    token_secret = '6OIPRG'
    channel_layer = get_channel_layer()
    async_to_sync(  channel_layer.group_send )( 
            'group_%s' % token_secret, 
            { 
                'type' :  'send_message',     
                'data' : 'empresa qualquer alterado na trigger' 
            }  
     )

def send_message( self, event ):
        message_to_be_sended = event[ 'data' ]
        channel_layer = get_channel_layer()
        async_to_sync( channel_layer.send )( text_data = json.dumps({
                'message' : message_to_be_sended
        }))
    
