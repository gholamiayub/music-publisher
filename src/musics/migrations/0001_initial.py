# Generated by Django 3.0.6 on 2020-06-08 15:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('cover', models.ImageField(blank=True, upload_to='covers/%Y/%m/%d/')),
                ('release_date', models.DateField(default=django.utils.timezone.now)),
                ('genre', models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop'), ('blues', 'Blues'), ('jazz', 'Jazz'), ('heavy-metal', 'Heavy metal')], max_length=20)),
                ('slug', models.SlugField(max_length=250, unique_for_date='release_date')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('cover', models.ImageField(blank=True, upload_to='musics-covers/%Y/%m/%d/')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('file', models.FileField(upload_to='songs')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='musics.Album')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='musics.Album')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musics.Band'),
        ),
    ]
