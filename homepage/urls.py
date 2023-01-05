from django.urls import path
from . import views
from django.urls import re_path as url
from accounts import models
from accounts.models import UserInfo

# homepage
app_name = 'homepage'

urlpatterns = [
url(r"^/$", views.HomeView.as_view(), name='home'),

]