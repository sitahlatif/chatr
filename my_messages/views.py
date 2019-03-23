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


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ChannelCreateAPIView(CreateAPIView):
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChannelListAPIView(ListAPIView):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()
    permission_classes = [IsAuthenticated, ]






class MessageCreateView(APIView):
    serializer_class = MessageCreateSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, channel_id):
        my_data = request.data
        serializer = self.serializer_class(data=my_data)
        if serializer.is_valid():
            valid_data = serializer.data
            new_data = {
                'message': valid_data['message'],
                'user': request.user,
                'channel': Channel.objects.get(id=channel_id)
            }
            Message.objects.create(**new_data)
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, ]



class JoindChannelView(APIView):
    permission_classes = [IsAuthenticated, ]

    def put(self, request, channel_id):
        channel=Channel.objects.get(id=channel_id)
        channel.members.add(User.objects.get(id=request.user.id))
        channel.save()
        return Response(ChannelSerializer(channel).data, status=HTTP_200_OK)



class UnJoindChannelView(APIView):
    permission_classes = [IsAuthenticated, ]

    def put(self, request, channel_id):
        channel=Channel.objects.get(id=channel_id)
        channel.members.remove(User.objects.get(id=request.user.id))
        channel.save()
        return Response(ChannelSerializer(channel).data, status=HTTP_200_OK)






class MessageListView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, channel_id):
        messages = Message.objects.filter(
            channel=Channel.objects.get(id=channel_id))
        latest = request.GET.get('latest')
        if latest:
            messages = messages.filter(timestamp__gt=latest)

        message_list = MessageListSerializer(messages, many=True).data

        return Response(message_list, status=status.HTTP_200_OK)


def deleteTheHamza(request):
    Message.objects.filter(user__username="hamsa").delete()
    return HttpResponse("LOOOOL")
