from django.urls import path
from .views import MessageListCreate, MessageRetrieveUpdateDelete, ReceiveMessage

urlpatterns = [
    path('messages/', MessageListCreate.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDelete.as_view(), name='message-detail'),
    path('receive-message/', ReceiveMessage.as_view(), name='receive-message'),
]
