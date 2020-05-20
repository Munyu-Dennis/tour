from django.urls import path
from . import views
from .views import (
    DestinationListView, 
    DestinationsDetailView,
    PackageListView,
    SearchDestination,
)
urlpatterns = [
    path('', DestinationListView.as_view(), name='home'),
    path('destination/<int:pk>/', DestinationsDetailView.as_view(), name='dest-detail'),
    path('buypackage/', PackageListView.as_view(), name='package'),
    path('search/', SearchDestination.as_view(), name='search'),
    path('about/', views.about, name='about')
]
