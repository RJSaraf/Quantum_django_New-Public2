from blog import views
from django.urls import path
from django.urls import re_path as url
from django.urls import reverse
from django.conf.urls import include

# blog
app_name = 'blog'


urlpatterns = [
    url(r"^$", views.PostListView.as_view(), name="post_list"),
    url(r"^post/(?P<pk>\d+)/$", views.PostDetailView.as_view(), name="post_detail"),
    url(r"^post/new/$", views.CreatePostView.as_view(), name="post_new"),
    url(r"^post/(?P<pk>\d+)/edit/$", views.PostUpdateView.as_view(), name="post_edit"),
    url(r"^post/(?P<pk>\d+)/remove/$", views.PostDeleteView.as_view(), name="post_remove"),
    url(r"^drafts/$", views.DraftListView.as_view(), name="post_draft_list"),
    ###########################################################################################
    url(r"^post/(?P<pk>\d+)/comment/$", views.add_comment_to_post, name="add_comment_to_post"),
    url(r"^comment/(?P<pk>\d+)/approve/$", views.comment_approve, name="comment_approve"),
    url(r"^comment/(?P<pk>\d+)/remove/$", views.comment_remove, name="comment_remove"),
    url(r"^comment/(?P<pk>\d+)/edit/$", views.CommentUpdateView.as_view(), name="comment_edit"),
    url(r"^post/(?P<pk>\d+)/publish/$", views.post_publish, name="post_publish"),
    ###########################################################################################
    url(r"^post/like/(?P<pk>\d+)/$", views.postlike, name="postlike"),
    
]


