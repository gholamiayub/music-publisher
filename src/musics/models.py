from django.db import models
from django.urls import reverse
from django.utils import timezone

from taggit.managers import TaggableManager


class Band(models.Model):
    name = models.CharField(max_length=250,
                            db_index=True)
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('musics:album',
                       args=[self.name])

class Album(models.Model):
    GENRE_CHOICES = (
    ('rock', 'Rock'),
    ('pop', 'Pop'),
    ('blues', 'Blues'),
    ('jazz', 'Jazz'),
    ('heavy-metal', 'Heavy metal'),
    )
    band = models.ForeignKey(Band,
                             on_delete=models.CASCADE,
                             related_name='albums')
    name = models.CharField(max_length=50, db_index=True)
    cover = models.ImageField(upload_to='covers/%Y/%m/%d/', blank=True)
    release_date = models.DateField(default=timezone.now)
    genre = models.CharField(max_length=20,
                             choices=GENRE_CHOICES)
    slug = models.SlugField(max_length=250,
                            unique_for_date='release_date')

    tags = TaggableManager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}-{self.band}'

    # def get_absolute_url(self):
    #     return reverse('musics:album_songs', args=[self.name])
    def get_absolute_url(self):
        return reverse('musics:album_songs',
                       kwargs={
                           'album_slug': self.slug,
                           'band_slug': self.band.slug})

class Song(models.Model):
    album = models.ForeignKey(Album,
                              related_name='musics',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    # cover = models.ImageField(upload_to='musics-covers/%Y/%m/%d/', blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    file = models.FileField(upload_to='songs')


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}-{self.album}'

    def get_absolute_url(self):
        return reverse('musics:album_songs',
                        args=[self.name])

class Comment(models.Model):
    album = models.ForeignKey(Album,
                              on_delete=models.CASCADE,
                              related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.album}'
