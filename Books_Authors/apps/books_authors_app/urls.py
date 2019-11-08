from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.add_book),
    url(r'^add_book_process$', views.add_book_process),
    url(r'^books/(?P<id>\d+)$', views.add_book_description),
    url(r'^books/book_description_process/(?P<book_id>\d+)$', views.book_description_process),
]
