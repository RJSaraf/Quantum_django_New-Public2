from django.urls import path
from django.conf.urls import url
from . import views
from . import models
from accounts.models import UserInfo
from django.contrib.auth.decorators import login_required

from django.contrib.auth import  views as auth_views

# accounts
app_name = 'accounts'

urlpatterns = [
#path('register' , views.register, name= 'register'),
#path('savedata' , views.savedata, name= 'savedata'),

#url(r"^login/$", views.login, name="login"),

url(r"^signup/$", views.SignUp.as_view(), name="signup"),
url(r"^login/$", auth_views.LoginView.as_view(template_name = 'login.html', success_url ='homepage:home'), name='login'),
url(r"^logout/$", views.logout, name="logout"),

url(r"^create/(?P<slug>[-\w]+)/$", views.UserInfoCreateView.as_view(), name="create_user_info"),  
url(r"^edit/(?P<slug>[-\w]+)/$", views.UserInfoUpdateView.as_view(), name='edit_user_info'),

url(r"^profile/Post/(?P<slug>[-\w]+)/$", views.UserView.as_view(), name='details'),
url(r"^profile/Friends/(?P<slug>[-\w]+)/$", views.UserViewFriends.as_view(), name='details_friends'),
url(r"^profile/Blogs/(?P<slug>[-\w]+)/$", views.UserViewBlogs.as_view(), name='details_blogs'),

url(r"^global_search/$", views.SearchUsers.as_view(), name="searchusers"),

 
]