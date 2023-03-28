from . import views
from django.urls import path
app_name = 'movie_app'

urlpatterns = [

    path('', views.index, name='index'),
    path('movie/<int:movie_id>', views.datas, name='datas'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update_movie, name='update_movie'),
    path('delete/<int:id>/', views.delete_movie, name='delete_movie')
]