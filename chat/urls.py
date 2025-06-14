from django.urls import path
from .views import inbox, send_message, view_message

urlpatterns = [
    path('', inbox, name='chat-inbox'),
    path('enviar/', send_message, name='chat-send'),
    path('mensaje/<int:pk>/', view_message, name='chat-view'),
]
