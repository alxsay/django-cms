from django.shortcuts import render

import pudb

def index( request ):
    return render( request, 'index.jinja', context = None )


def card1( request ):
    #pudb.set_trace()
    return render( request, 'card1.jinja', context = None )


def card2( request ):
    return render( request, 'card2.jinja', context = None )


def card3( request ):
    return render( request, 'extras/card3.jinja', context = None )



