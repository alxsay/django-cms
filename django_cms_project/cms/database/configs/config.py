#!/usr/bin/python
"""
arquivo: app.database.config.py
autor: Saymon de Oliveira Souza ( saymon.souza@cogni.group )
propósito: Carrega as credenciais de conexão com o banco de dados definidas em database.ini

data criação: xx/11/2018
última atualização: xx/11/2018

"""

from configparser import ConfigParser

def configs( filename = 'cms/database/configs/database.ini', section = 'postgresql' ):
    parser = ConfigParser()
    parser.read( filename )
 
    db = {}
    if parser.has_section( section ):
        params = parser.items( section )
        for param in params:
            db[ param[ 0 ] ] = param[ 1 ]
    else:
        raise Exception( 'Section {0} not found in the {1} file'.format( section, filename ) )
 
    return db
