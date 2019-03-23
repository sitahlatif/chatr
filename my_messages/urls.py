from django.urls import path
from .views import (
    MessageCreateView,
    MessageListView,
    UserLoginAPIView,
    UserCreateAPIView,
    ChannelCreateAPIView,
    ChannelListAPIView,
    JoindChannelView,
    UnJoindChannelView,
    UserListAPIView
)
urlpatterns = [
    path('', ChannelListAPIView.as_view(), name='channel-list'),
    path('create/', ChannelCreateAPIView.as_view(), name='channel-create'),
    path('<int:channel_id>/', MessageListView.as_view(), name='message-list'),
    path('<int:channel_id>/send/',
         MessageCreateView.as_view(), name='message-create'),
    path('<int:channel_id>/add',JoindChannelView.as_view(), name='member-append'),
    path('<int:channel_id>/delete',UnJoindChannelView.as_view(), name='member-remove'),
    path('user/',UserListAPIView.as_view(), name='user-list')



]
