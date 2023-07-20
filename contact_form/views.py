from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .forms import CaptchaForm

# Render the contact page

def contact_form(request):
    captcha = CaptchaForm
    context = {
        'captcha': captcha
        }
    return render(request, 'contact_form.html', context)

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
        captcha = CaptchaForm(request.POST)
        if captcha.is_valid():
            name = request.POST['name']
            email_data = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']

            print(name, email_data, subject, message)

            template = render_to_string('email_template.html', {
                'name': name,
                'email_data': email_data,
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

            # Adds the success message with each line of the template
            success_message = render_to_string('alert_success.html', {
                'name': name,
                'email_data': email_data,
                'subject': subject,
                'message': message
            })

            messages.success(request, success_message)

            return redirect('contact_form')
        else:
            context = {
                'captcha': captcha
            }
            return render(request, 'contact_form.html', context)

