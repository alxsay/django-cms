from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment


"""

This enables us to use Django template tags like {% url ‘index’ %} 
or {% static ‘path/to/static/file.js’ %} in our Jinja2 templates. 
As you can see, these template tags use the actual functions provided by Django. 
Following the Jinja2 way of calling functions in template you can use them like this:

Django’s:

{% url ‘index’ variable %}
is equivalent to:

{{url(‘index’, args=[variable])}}
in Jinja2. And for named variables you can use:

{{url('index', kwargs={'variable_key':variable}}}
Django’s

{% static ‘path’ %}
is equivalent to

{{ static(‘path’)}}

As you have probably already noticed you can basically add any functions to Jinja2 environment 
by adding them to jinja2.py file to make them usable in templates.

"""

def environment( **options ):
    env = Environment( **options )
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })

    return env