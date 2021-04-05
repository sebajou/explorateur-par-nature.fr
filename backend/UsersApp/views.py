from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UsersSerializer, BadgeSerializer, TributSerializer, ChildSerializer, TrophiesSerializer, \
    TutorLinkSerializer
from .models import Users, Badge, Tribut, Child, Trophies, TutorLink
from rest_framework.permissions import IsAuthenticated

# Create your views here.


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
