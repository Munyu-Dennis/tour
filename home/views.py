from django.shortcuts import render
from .models import Destinations
from django.db.models import Q
from django.views.generic import ( 
            ListView, 
            DetailView,
            CreateView,
            UpdateView,
            DeleteView
            
)

def home(request):
    return render(request, 'home/home.html')

class DestinationListView(ListView):
    model = Destinations
    template_name = 'home/home.html'#<app>/<model>_<view_type>.html
    context_object_name = 'dests'
    ordering = ['price']
    paginate_by = 6
    '''def get_queryset(self):
        diplay = { "tit": Post.title,
                     "tit": Comment.objects.all()}
        return diplay'''
    
class PackageListView(ListView):
    model = Destinations
    template_name = 'home/package.html'#<app>/<model>_<view_type>.html
    context_object_name = 'dests'
    ordering = ['price']
    paginate_by = 3

class SearchDestination(ListView):
    model = Destinations
    template_name = 'home/search.html'
    def get_queryset(self):
        query = self.request.GET.get('cp')
        object_list = Destinations.objects.filter( Q(name__icontains=query) | Q(price__icontains=query))
        return object_list
    
class DestinationsDetailView(DetailView):
    model = Destinations

def about(request):
    return render(request, 'home/about.html')