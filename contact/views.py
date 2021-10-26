from django.shortcuts import render

# Create your views here.
from .forms import ContactForm

# add to your views


def contact(request):
    form_class = ContactForm

    return render(request, 'contact/contact.html', {
        'form': form_class,
    })
