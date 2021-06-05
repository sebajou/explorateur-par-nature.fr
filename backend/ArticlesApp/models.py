from django.db import models
from UsersApp.models import Badge, Users


# Create your models here.


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    id_badge = models.ForeignKey('UsersApp.Badge', models.DO_NOTHING, db_column='id_badge')
    title = models.CharField(max_length=60)
    objectif = models.CharField(max_length=150)
    content = models.TextField()
    publication_date = models.DateTimeField()
    edition_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'article'


class Bibliography(models.Model):
    id_bibliography = models.AutoField(primary_key=True)
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='id_article')
    id_users = models.ForeignKey('UsersApp.Users', models.DO_NOTHING, db_column='id')

    class Meta:
        managed = True
        db_table = 'bibliography'
        unique_together = (('id_bibliography', 'id_article', 'id_users'),)


class Equipment(models.Model):
    id_equipment = models.AutoField(primary_key=True)
    text = models.CharField(max_length=150)
    quantity = models.FloatField()
    unity = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'equipment'


class Image(models.Model):
    id_image = models.AutoField(primary_key=True)
    imagefield = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=70, blank=True, null=True)
    authors = models.CharField(max_length=60, blank=True, null=True)
    title = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'image'


class ListEquipment(models.Model):
    id_list_equipment = models.AutoField(primary_key=True)
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='id_article')
    id_equipment = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='id_equipment')

    class Meta:
        managed = True
        db_table = 'list_equipment'
        unique_together = (('id_list_equipment', 'id_article', 'id_equipment'),)


class ListImage(models.Model):
    id_list_image = models.AutoField(primary_key=True)
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='id_article')
    id_image = models.ForeignKey(Image, models.DO_NOTHING, db_column='id_image')

    class Meta:
        managed = True
        db_table = 'list_image'


class ListVideo(models.Model):
    id_list_video = models.AutoField(primary_key=True)
    id_video = models.ForeignKey('Video', models.DO_NOTHING, db_column='id_video')
    id_article = models.ForeignKey(Article, models.DO_NOTHING, db_column='id_article')

    class Meta:
        managed = True
        db_table = 'list_video'


class Video(models.Model):
    id_video = models.AutoField(primary_key=True)
    videofield = models.CharField(max_length=100)
    description = models.CharField(max_length=70)
    authors = models.CharField(max_length=60)
    title = models.CharField(max_length=70)

    class Meta:
        managed = True
        db_table = 'video'
