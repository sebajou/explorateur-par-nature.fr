from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArticleSerializer, BibliographySerializer, EquipmentSerializer, ImageSerializer, \
    ListImageSerializer, ListEquipmentSerializer, ListVideoSerializer, VideoSerializer
from .models import Article, Bibliography, Equipment, Image, ListImage, ListEquipment, ListVideo, Video
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ArticleView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class BibliographyView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BibliographySerializer
    queryset = Bibliography.objects.all()


class EquipmentView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()


class ImageView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ListImageView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListImageSerializer
    queryset = ListImage.objects.all()


class ListEquipmentView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListEquipmentSerializer
    queryset = ListEquipment.objects.all()


class ListVideoView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListVideoSerializer
    queryset = ListVideo.objects.all()


class VideoView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
