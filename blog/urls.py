from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('like-post/<int:post_id>/', views.like_post, name='like_post'),
    path('like-comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('categorie/<slug:slug>/', views.CategoryPostsView.as_view(), name='category_posts'),
    path('tag/<slug:slug>/', views.TagPostsView.as_view(), name='tag_posts'),
    path('recherche/', views.SearchView.as_view(), name='search'),
] 