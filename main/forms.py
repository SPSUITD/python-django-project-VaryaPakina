from django import forms

from .models import ChannelMessage, Message


class ChannelMessageForm(forms.ModelForm):
  class Meta:
    model = ChannelMessage
    fields = ('text',)


class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ('text',)
