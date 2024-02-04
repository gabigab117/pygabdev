from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Objet", max_length=20)
    text = forms.CharField(label="message", max_length=2000, widget=forms.Textarea)
    security = ReCaptchaField(label="Sécurité", widget=ReCaptchaV2Checkbox(
        attrs={"style": "display: flex;align_items: center;justify-content: center;"}))
