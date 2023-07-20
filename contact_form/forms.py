from django import forms
from captcha.fields import ReCaptchaField

# The captcha form for validate
class CaptchaForm(forms.Form):
    captcha = ReCaptchaField()


