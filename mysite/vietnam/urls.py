from django.urls import path

from . import views


app_name = "vietnam"
urlpatterns = [
    path('', views.list_vietnam, name='list'),
    path('get/<int:pk>/', views.get_vietnam, name='get'),
    path('create/', views.create_vietnam, name='create'),
    path('put/<int:pk>/', views.put_vietnam, name='update'),
    path('delete/<int:pk>/', views.delete_vietnam, name='delete')
]
