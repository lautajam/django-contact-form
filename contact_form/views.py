from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def contact_form(request):
    return render(request, 'contact_form.html')

def contact(request):
    pass