from django.urls import path
from . import views

app_name = 'musics'

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('bands/', views.BandList.as_view(), name='band_albums'),
    path('albums/<name>/', views.AlbumList.as_view(), name='album'),
    # path('bands/albums/songs/<name>/', views.album_songs, name='album_songs'),
    path('<band_slug>/<album_slug>/songs/', views.album_songs, name='album_songs'),
    # path('bands/albums/songs/<name>/', views.SongList.as_view(), name='album_songs'),
    path('tag/<slug:tag_slug>/', views.AlbumList.as_view(), name='songs_list_by_tag'),
    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
    path('success/', views.success_view, name='success'),
]
