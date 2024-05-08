from .models import Link

from django.forms import ModelForm

class LinkModelForm(ModelForm):
    class Meta:
        model = Link
        fields = ['url']