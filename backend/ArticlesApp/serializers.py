from rest_framework import serializers
from .models import Article, Bibliography, Equipment, Image, ListImage, ListEquipment, ListVideo, Video


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id_article', 'title', 'objectif', 'content', 'publication_date', 'edition_date', 'id_badge')
        read_only_fields = ['id_article', 'publication_date', 'edition_date']


class BibliographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliography
        fields = ('id_bibliography', 'id_article', 'id_users')
        read_only_fields = ['id_bibliography']


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id_equipment', 'text', 'quantity', 'unity')
        read_only_fields = ['id_equipment']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id_image', 'imagefield', 'description', 'authors', 'title')
        read_only_fields = ['id_image']


class ListImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListImage
        fields = ('id_list_image', 'id_article', 'id_image')


class ListEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListEquipment
        fields = ('id_list_equipment', 'id_article', 'id_equipment')


class ListVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListVideo
        fields = ('id_list_video', 'id_article', 'id_video')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id_video', 'viedofield', 'description', 'authors', 'title')
        read_only_fields = ['id_video']
