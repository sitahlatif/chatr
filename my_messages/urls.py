from django.urls import path
from .views import (
    MessageCreateView,
    MessageListView,
    UserLoginAPIView,
    UserCreateAPIView,
    ChannelCreateAPIView,
    ChannelListAPIView,
    JoindChannelView
)
urlpatterns = [
    path('', ChannelListAPIView.as_view(), name='channel-list'),
    path('create/', ChannelCreateAPIView.as_view(), name='channel-create'),
    path('<int:channel_id>/', MessageListView.as_view(), name='message-list'),
    path('<int:channel_id>/send/',
         MessageCreateView.as_view(), name='message-create'),
    path('<int:channel_id>/update',JoindChannelView.as_view(), name='member-append'),
    #create a URL that accepts a channelID example .../id/add/
]
