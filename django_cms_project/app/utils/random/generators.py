#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
arquivo: app.utilities.generators.py
autor: Saymon de Oliveira Souza ( saymon.souza@cogni.group )
propósito: srcript responsável pela geração randômica de tokens
data criação: 07/11/2018
última atualização: xx/11/2018

"""

import random
import string

def generate_random_string( size = 6, chars = string.ascii_uppercase + string.digits ):
    return ''.join( random.choice( chars ) for _ in range( size ) )