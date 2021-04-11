# Generated by Django 3.2 on 2021-04-09 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id_article', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('objectif', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('publication_date', models.DateTimeField()),
                ('edition_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'article',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id_equipment', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=150)),
                ('quantity', models.FloatField()),
                ('unity', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'equipment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id_image', models.AutoField(primary_key=True, serialize=False)),
                ('imagefield', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=70, null=True)),
                ('authors', models.CharField(blank=True, max_length=60, null=True)),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
            ],
            options={
                'db_table': 'image',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id_video', models.AutoField(primary_key=True, serialize=False)),
                ('videofield', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=70)),
                ('authors', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'video',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ListVideo',
            fields=[
                ('id_list_video', models.AutoField(primary_key=True, serialize=False)),
                ('id_article', models.ForeignKey(db_column='id_article', on_delete=django.db.models.deletion.DO_NOTHING, to='ArticlesApp.article')),
                ('id_video', models.ForeignKey(db_column='id_video', on_delete=django.db.models.deletion.DO_NOTHING, to='ArticlesApp.video')),
            ],
            options={
                'db_table': 'list_video',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ListImage',
            fields=[
                ('id_list_image', models.AutoField(primary_key=True, serialize=False)),
                ('id_article', models.ForeignKey(db_column='id_article', on_delete=django.db.models.deletion.DO_NOTHING, to='ArticlesApp.article')),
                ('id_image', models.ForeignKey(db_column='id_image', on_delete=django.db.models.deletion.DO_NOTHING, to='ArticlesApp.image')),
            ],
            options={
                'db_table': 'list_image',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ListEquipment',
            fields=[
                ('id_list_equipment', models.AutoField(primary_key=True, serialize=False)),
                ('id_article', models.ForeignKey(db_column='id_article', on_delete=django.db.models.deletion.DO_NOTHING, to='ArticlesApp.article')),
                ('id_equipment', models.ForeignKey(db_column='id_equipment', on_delete=django.db.models.deletion.DO_NOTHING, to='ArticlesApp.equipment')),
            ],
            options={
                'db_table': 'list_equipment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Bibliography',
            fields=[
                ('id_bibliography', models.AutoField(primary_key=True, serialize=False)),
                ('id_article', models.ForeignKey(db_column='id_article', on_delete=django.db.models.deletion.DO_NOTHING, to='ArticlesApp.article')),
            ],
            options={
                'db_table': 'bibliography',
                'managed': True,
            },
        ),
    ]
