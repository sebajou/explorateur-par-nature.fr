from rest_framework import serializers
from .models import Myuser, Badge, Tribut, Child, Trophies, TutorLink


class MyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myuser
        fields = ('is_superuser', 'is_staff', 'is_active', 'id_myuser', 'username', 'first_name',
                  'last_name', 'image_profil', 'is_author', 'last_login', 'date_joined', 'email', 'id_tribut')


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ('id_badge', 'title', 'category', 'level', 'type', 'filefield')


class TributSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tribut
        fields = ('id_tribut', 'tribut_name')


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('id_child', 'username', 'first_name', 'last_name', 'image_profil', 'last_login', 'date_jointed',
                  'pwd', 'id_tribut')


class TrophiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophies
        fields = ('id_trophies', 'id_badge', 'id_child')


class TutorLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorLink
        fields = ('id_tutor_link', 'id_child', 'id_myuser')
