# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    id_badge = models.ForeignKey('Badge', models.DO_NOTHING, db_column='id_badge')
    title = models.CharField(max_length=60)
    objectif = models.CharField(max_length=150)
    content = models.TextField()
    publication_date = models.DateTimeField()
    edition_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'article'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Badge(models.Model):
    id_badge = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    level = models.IntegerField()
    type = models.CharField(max_length=40)
    filefield = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'badge'


class Bibliography(models.Model):
    id_bibliography = models.AutoField(primary_key=True)
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='id_article')
    id_myuser = models.ForeignKey('Myuser', models.DO_NOTHING, db_column='id_myuser')

    class Meta:
        managed = False
        db_table = 'bibliography'
        unique_together = (('id_bibliography', 'id_article', 'id_myuser'),)


class Child(models.Model):
    id_child = models.AutoField(primary_key=True)
    id_tribut = models.ForeignKey('Tribut', models.DO_NOTHING, db_column='id_tribut')
    username = models.CharField(max_length=70)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image_profil = models.CharField(max_length=100, blank=True, null=True)
    last_login = models.DateTimeField()
    date_jointed = models.DateTimeField()
    pwd = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'child'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equipment(models.Model):
    id_equipment = models.AutoField(primary_key=True)
    text = models.CharField(max_length=150)
    quantity = models.FloatField()
    unity = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'equipment'


class Image(models.Model):
    id_image = models.AutoField(primary_key=True)
    imagefield = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=70, blank=True, null=True)
    authors = models.CharField(max_length=60, blank=True, null=True)
    title = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'


class ListEquipment(models.Model):
    id_list_equipment = models.AutoField(primary_key=True)
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='id_article')
    id_equipment = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='id_equipment')

    class Meta:
        managed = False
        db_table = 'list_equipment'
        unique_together = (('id_list_equipment', 'id_article', 'id_equipment'),)


class ListImage(models.Model):
    id_list_image = models.AutoField(primary_key=True)
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='id_article')
    id_image = models.ForeignKey(Image, models.DO_NOTHING, db_column='id_image')

    class Meta:
        managed = False
        db_table = 'list_image'


class ListVideo(models.Model):
    id_list_video = models.AutoField(primary_key=True)
    id_video = models.ForeignKey('Video', models.DO_NOTHING, db_column='id_video')
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='id_article')

    class Meta:
        managed = False
        db_table = 'list_video'


class Myuser(models.Model):
    id_myuser = models.AutoField(primary_key=True)
    id_tribut = models.ForeignKey('Tribut', models.DO_NOTHING, db_column='id_tribut')
    username = models.CharField(max_length=70)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    image_profil = models.CharField(max_length=100, blank=True, null=True)
    is_author = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    hash_pwd = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'myuser'


class Tribut(models.Model):
    id_tribut = models.AutoField(primary_key=True)
    tribut_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tribut'


class Trophies(models.Model):
    id_trophies = models.AutoField(primary_key=True)
    id_child = models.ForeignKey(Child, models.DO_NOTHING, db_column='id_child')
    id_badge = models.ForeignKey(Badge, models.DO_NOTHING, db_column='id_badge')

    class Meta:
        managed = False
        db_table = 'trophies'


class TutorLink(models.Model):
    id_tutor_link = models.AutoField(primary_key=True)
    id_child = models.ForeignKey(Child, models.DO_NOTHING, db_column='id_child')
    id_myuser = models.ForeignKey(Myuser, models.DO_NOTHING, db_column='id_myuser')

    class Meta:
        managed = False
        db_table = 'tutor_link'


class Video(models.Model):
    id_video = models.AutoField(primary_key=True)
    videofield = models.CharField(max_length=100)
    description = models.CharField(max_length=70)
    authors = models.CharField(max_length=60)
    title = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'video'
