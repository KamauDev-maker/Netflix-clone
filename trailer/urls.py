from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search/', views.search, name = 'search'),
    path('movie/<int:movie_id>/', views.view_movie_detail, name = 'moviedetail'),
]