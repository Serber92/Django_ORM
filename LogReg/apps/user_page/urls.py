from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration_process$', views.registration),
    url(r'^login_process$', views.login),
    url(r'^success$', views.success),
    url(r'^logout', views.logout),
    url(r'^post_message', views.post_message),
    url(r'^post_comment', views.post_comment),
    url(r'^delete/message/(?P<message_id>\d+)$', views.delete_message)
]
