from django.urls import path, re_path
from blog import views


urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    re_path('post/(?P<pk>\d+)', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    re_path('post/(?P<pk>\d+)/edit/', views.PostUpdateView.as_view(),
         name='post_edit'),
    re_path('post/(?P<pk>\d+)/remove/', views.PostDeleteView.as_view(),
         name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    re_path('post/(?P<pk>\d+)/comment/', views.add_comment_to_post, name='add_comment_to_post')
]
