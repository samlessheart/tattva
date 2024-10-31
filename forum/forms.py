from django import forms
from django.forms import (fields, widgets, Textarea, NumberInput, Select, DateField)
from .models import *





class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields  ="__all__"


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Forum_reply
        fields  ="__all__"