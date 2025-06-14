from django.urls import path
from .views import home, about, post_list, post_detail, post_create, post_update, post_delete

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('anotaciones/', post_list, name='post-list'),
    path('anotaciones/<int:pk>/', post_detail, name='post-detail'),
    path('anotaciones/create/', post_create, name='post-create'),
    path('anotaciones/<int:pk>/edit/', post_update, name='post-update'),
    path('anotaciones/<int:pk>/delete/', post_delete, name='post-delete'),
]
