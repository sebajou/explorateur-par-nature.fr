from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import UsersSerializer, BadgeSerializer, TributSerializer, ChildSerializer, TrophiesSerializer, \
    TutorLinkSerializer
from .models import Users, Badge, Tribut, Child, Trophies, TutorLink
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class HelloWorldView(APIView):

    def get(self, request):
        return Response(data={"hello": "world"}, status=status.HTTP_200_OK)


class CustomUserCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format='json'):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            print('token : ', request.data["refresh_token"])
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print('token : ', request.data["refresh_token"])
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UsersView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class BadgeView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()


class TributView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TributSerializer
    queryset = Tribut.objects.all()


class ChildView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChildSerializer
    queryset = Child.objects.all()


class TrophiesView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TrophiesSerializer
    queryset = Trophies.objects.all()


class TutorLinkView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TutorLinkSerializer
    queryset = TutorLink.objects.all()
