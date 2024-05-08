
from django.contrib import admin
from django.urls import path
from . import views
app_name='email'
urlpatterns = [
    path('email/',views.send_email,name='send_email'),
    path('email_views/',views.views_email,name='send_email_views')
]
