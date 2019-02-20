from django.shortcuts import render

def index( request ):
    return render( request, 'index.jinja', context = None )


def card1( request ):
    return render( request, 'card1.jinja', context = None )


def card2( request ):
    return render( request, 'card2.jinja', context = None )



