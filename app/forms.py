from django import forms
from app.models import *


class Topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class Webpageform(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'


class Accessrecordform(forms.ModelForm):
    class Meta:
        model=Accessrecord
        fields='__all__'