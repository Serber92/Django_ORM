from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.new),
    url(r'^shows/new/process$', views.new_process),
    url(r'^shows/(?P<show_index>\d+)$', views.shows_info),
    url(r'^shows/(?P<show_id>\d+)/delete$', views.delete),
    url(r'^shows/(?P<show_id>\d+)/edit', views.edit),
    url(r'^shows/edit/process', views.edit_process),
]