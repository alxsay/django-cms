"""
arquivo: app.middlewares.py
autor: Saymon de Oliveira Souza ( saymon.souza@cogni.group )
propósito: Processa request a app

data criação: xx/11/2018
última atualização: xx/11/2018
"""

class AppMiddleware:
    
    def __init__( self, get_response ):
        self.get_response = get_response

    def __call__( self, request ):
        response = self.get_response( request )
        print( "\"Tudo posso naquEle que me fortalece\". ( Filipenses 4:13 )" )
        return response