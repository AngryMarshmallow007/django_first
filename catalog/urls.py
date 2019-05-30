from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/$', views.GameListView.as_view(), name='games'),
    url(r'^game/(?P<pk>\d+)$', views.GameDetailView.as_view(), name='game-detail'),
]

