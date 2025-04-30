from django.urls import path
from . import views

app_name = 'pages_slug'

urlpatterns = [
    path('<slug:slug>/', views.page_detail, name='page_detail'),
] 