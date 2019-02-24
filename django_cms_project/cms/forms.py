from django import forms
from django.forms import ModelForm

from cms.models import CmsPost

class NameForm( forms.Form ):
    your_name = forms.CharField( label = 'Your name', max_length = 100 )


class ContactForm( forms.Form ):
    subject = forms.CharField( max_length = 100 )
    message = forms.CharField( widget = forms.Textarea )
    sender = forms.EmailField()
    cc_myself = forms.BooleanField( required = False )

class PostForm( ModelForm ):

    class Meta:
        model = CmsPost
        #fields = ['pub_date', 'headline', 'content', 'reporter']
        fields = '__all__'

"""
<label for="your_name">Your name: </label>
<input id="your_name" type="text" name="your_name" maxlength="100" required>

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

# no template:
<form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>
"""