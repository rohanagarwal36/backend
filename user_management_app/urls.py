from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^logout/$', views.Logout.as_view()),
    url(r'^user/$', views.UserAPI.as_view({'post': 'create'})),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserAPI.as_view({'get': 'retrieve', 'put': 'update'}))
]
