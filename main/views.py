from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import forms, logout, get_user_model
from django.db.models import Q

from .forms import MessageForm, ChannelMessageForm
from .models import Message, Channel, ChannelMessage


User = get_user_model()


def index(request):
    context = {}
    if request.user.is_authenticated:
      context['users'] = User.objects.all()
      context['channels'] = Channel.objects.all()
      return render(request, 'index.html', context)
    else:
      return redirect('login')


def channel_page(request, title):
  channel = get_object_or_404(Channel, title=title)
  if request.method == 'POST':
    form = ChannelMessageForm(request.POST)
    if form.is_valid():
      message = form.save(commit=False)
      message.channel = channel
      message.author = request.user
      message.save()
    return redirect('channel', title=channel.title)

  messages = ChannelMessage.objects.filter(
    channel=channel
  ).order_by('publication_time')

  return render(request, 'channel.html', {'messages': messages})

def dialog_page(request, pk):
  user = get_object_or_404(User, pk=pk)
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      message = form.save(commit=False)
      message.author = request.user
      message.user_to = user
      message.save()
    return redirect('dialog', pk=pk)
  
  messages = Message.objects.filter(
    Q(author=request.user,user_to=user) |
    Q(author=user,user_to=request.user)  
  ).order_by('publication_time')

  return render(request, 'dialog.html', {'messages': messages})

def signup(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')
