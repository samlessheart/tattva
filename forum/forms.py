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
        fields  = ['reply_text']

    # def save(self, commit =True):
    #     reply = super().save(commit= False)
    #     if self.request and self.request.user.is_authenticated:
    #         reply.created_by = self.request.user
    #         reply.forum = self.request.resolver_match.kwargs['pk']
        
    #     if commit:
    #         reply.save()
    #     pass