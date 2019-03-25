from .serializers import (
    MessageListSerializer,
    MessageCreateSerializer,
    UserCreateSerializer,
    UserLoginSerializer,
    ChannelSerializer,
    UserSerializer

)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from .models import Message, Channel
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse

# this view is for the UserLogin
class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#this view for user create 
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

#this view for channel create
class ChannelCreateAPIView(CreateAPIView):
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#this view for channel list
class ChannelListAPIView(ListAPIView):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()
    permission_classes = [IsAuthenticated, ]

#this view for creating message in the chatr
class MessageCreateView(APIView):
    serializer_class = MessageCreateSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, channel_id):
        my_data = request.data
        serializer = self.serializer_class(data=my_data)
        if serializer.is_valid():
            valid_data = serializer.data
            new_data = {
                'message': valid_data['message'],# get the message written
                'user': request.user,# get the user 
                'channel': Channel.objects.get(id=channel_id)#get the channel id
            }
            Message.objects.create(**new_data)
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


#this view for the user list
class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    #this line is to get the all objects of user 
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, ]


#this view for joining channel  
class JoindChannelView(APIView):
    permission_classes = [IsAuthenticated, ]

    def put(self, request, channel_id):
        #this line to get the channel id 
        channel=Channel.objects.get(id=channel_id)
        #this line is to add user to the members of channel
        channel.members.add(User.objects.get(id=request.user.id))
        #to save the channel
        channel.save()
        return Response(ChannelSerializer(channel).data, status=HTTP_200_OK)


#this view for unjoind channel
class UnJoindChannelView(APIView):
    permission_classes = [IsAuthenticated, ]

    def put(self, request, channel_id):
        #this line to get the channel id 
        channel=Channel.objects.get(id=channel_id)

        #this line to remove the user from members of the channel 
        channel.members.remove(User.objects.get(id=request.user.id))

        #this line to save the channel 
        channel.save()
        return Response(ChannelSerializer(channel).data, status=HTTP_200_OK)


# this view for displaying message list 
class MessageListView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, channel_id):
        messages = Message.objects.filter(
            channel=Channel.objects.get(id=channel_id))
        # to get the latest message 
        latest = request.GET.get('latest')
        #filter the message which is greater than the latest message
        if latest:
            messages = messages.filter(timestamp__gt=latest)

        message_list = MessageListSerializer(messages, many=True).data

        return Response(message_list, status=status.HTTP_200_OK)


def deleteTheHamza(request):
    Message.objects.filter(user__username="hamsa").delete()
    return HttpResponse("LOOOOL")
