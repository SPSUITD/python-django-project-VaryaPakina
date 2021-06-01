from django.urls import path
from django.contrib.auth.views import LoginView


from .views import index, signup, channel_page, dialog_page, logout_view

urlpatterns = [
  path('', index, name='index'),
  path('login/', LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', logout_view, name='logout'),
  path('signup/', signup, name='signup'),
  path('channel/<str:title>/', channel_page, name='channel'),
  path('dialog/<int:pk>/', dialog_page, name='dialog'),
]