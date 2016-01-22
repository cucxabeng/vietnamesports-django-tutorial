from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /food/5/
    url(r'^food/(?P<food_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
]