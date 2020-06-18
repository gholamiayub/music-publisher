from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .models import Album, Band, Song, Comment
from .forms import CommentForm, ContactForm

from taggit.models import Tag


class BandList(ListView):
    model = Band
    template_name = 'musics/band_list.html'
    context_object_name = 'bands'
    paginate_by = 10

class AlbumList(ListView):
    template_name = 'musics/album_list.html'
    context_object_name = 'albums'
    paginate_by = 10

    def get_queryset(self):

        band = Band.objects.get(name=self.kwargs['name'])
        albums = band.albums.all()
        return albums

# def album_songs(request, name):
#
#     album = Album.objects.get(name=name)
#     songs = album.musics.all()
#
#     #  List of active comment for this album
#     comments = album.comments.filter(active=True)
#
#     new_comment = None
# i changed the slug url 
def album_songs(request, album_slug, band_slug):

    album = Album.objects.get(slug=album_slug)
    songs = album.musics.all()

    #  List of active comment for this album
    comments = album.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            # Assign the current album to the comment
            new_comment.album = album
            new_comment.save()
            return redirect(reverse('musics:album_songs', args=[name]))
    else:
        form = CommentForm()

    return render(request,
                  'musics/song_list.html',
                  {'songs': songs,
                   'album': album,
                   'comments': comments,
                   'new_comment': new_comment,
                   'form': form})

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SearchResultsListView(ListView):
    model = Song
    context_object_name = 'song_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Song.objects.filter(name__icontains=query)


def contact_view(request):
    print('this is contact view')
    if request.method == 'post':
        print('request.method == post')
        contact_form = ContactForm(data=request.POST)
        if contact_form .is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name)
            # try:
            #     send_mail(message, name, email, ['admin@gmail.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        contact_form  = ContactForm()
    return render(request, 'contact_us.html', {'form': contact_form })

def success_view(request):
    return HttpResponse('Success! Thank you for your message.')
