from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import MyuserSerializer, BadgeSerializer, TributSerializer, ChildSerializer, TrophiesSerializer, \
    TutorLinkSerializer
from .models import Myuser, Badge, Tribut, Child, Trophies, TutorLink
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.


class MyuserView(viewsets.ModelViewSet, APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = MyuserSerializer
    queryset = Myuser.objects.all()

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


class BadgeView(viewsets.ModelViewSet):
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()


class TributView(viewsets.ModelViewSet):
    serializer_class = TributSerializer
    queryset = Tribut.objects.all()


class ChildView(viewsets.ModelViewSet):
    serializer_class = ChildSerializer
    queryset = Child.objects.all()


class TrophiesView(viewsets.ModelViewSet):
    serializer_class = TrophiesSerializer
    queryset = Trophies.objects.all()


class TutorLinkView(viewsets.ModelViewSet):
    serializer_class = TutorLinkSerializer
    queryset = TutorLink.objects.all()
