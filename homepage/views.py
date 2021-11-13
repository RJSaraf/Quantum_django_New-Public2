from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from accounts import models
from accounts.models import UserInfo
from accounts.forms import UserForm

from TheSocialClub.models import Group, GroupMember, Post, FriendsList, FriendRequest
from django.contrib.auth.models import AnonymousUser

# Create your views here.
# homepage

class HomeView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user if type(self.request.user) is not AnonymousUser else None
            try:
                user_profile = UserInfo.objects.get(user=user)

            except UserInfo.DoesNotExist:
                user_profile = UserInfo.objects.create(user=user)
                user_profile.save()

            try:
                friend_list = FriendsList.objects.get(user=self.request.user)

            except FriendsList.DoesNotExist:
                friend_list = FriendsList.objects.create(user=self.request.user)
                friend_list.save()

            try:
                context = super(HomeView, self).get_context_data(*args, **kwargs)
                context['friendlist'] = FriendsList.objects.filter(user_id=user.id)
                context['friendrequest'] = FriendRequest.objects.filter(reciever=user, is_active=True)
                return context

            except :
                pass
        
        else:
            None