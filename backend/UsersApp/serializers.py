from rest_framework import serializers
from .models import Users, Badge, Tribut, Child, Trophies, TutorLink


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('is_superuser', 'is_staff', 'is_active', 'id_users', 'username', 'first_name',
                  'last_name', 'image_profil', 'is_author', 'last_login', 'date_joined', 'email', 'id_tribut')
        read_only_fields = ['id_users', 'is_superuser', 'is_staff', 'is_active', 'last_login', 'date_joined',
                            'is_author']


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ('id_badge', 'title', 'category', 'level', 'type', 'filefield')
        read_only_fields = ['id_badge']


class TributSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tribut
        fields = ('id_tribut', 'tribut_name')
        read_only_fields = ['id_tribut']


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('id_child', 'username', 'first_name', 'last_name', 'image_profil', 'last_login', 'date_jointed',
                  'pwd', 'id_tribut')
        read_only_fields = ['id_child', 'last_login', 'date_jointed']


class TrophiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophies
        fields = ('id_trophies', 'id_badge', 'id_child')


class TutorLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorLink
        fields = ('id_tutor_link', 'id_child', 'id_users')
