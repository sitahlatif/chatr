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
    #path for channel list api view 
    path('', ChannelListAPIView.as_view(), name='channel-list'),

    #path for create channel 
    path('create/', ChannelCreateAPIView.as_view(), name='channel-create'),

    #path for the message list view 
    path('<int:channel_id>/', MessageListView.as_view(), name='message-list'),

    #path for the create message 
    path('<int:channel_id>/send/',
         MessageCreateView.as_view(), name='message-create'),

    #path for joind channel view  
    path('<int:channel_id>/add',JoindChannelView.as_view(), name='member-append'),

    #path for unjoind channel view 
    path('<int:channel_id>/delete',UnJoindChannelView.as_view(), name='member-remove'),
    
    #path for userlist view 
    path('user/',UserListAPIView.as_view(), name='user-list'),



]
