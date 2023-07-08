from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

# Create your views here.

# Render the contact page
def contact_form(request):
    return render(request, 'contact_form.html')

# Process the contact form and send an email.
def contact(request):

    """
    Process the contact form and send an email.

    Args:
        request (HttpRequest): the HTTP request received.

    Returns:
        HttpResponseRedirect: Redirects to the contact form page whit message succes

    """

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # print(name, email, subject, message)

        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['test.user.email.07.2023@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'The mail has been sent.')

        return redirect('contact_form')