from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.LoginAPIView.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^user/$', views.UserAPIViewSet.as_view({'post': 'create'}), name='create-user'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserAPIViewSet.as_view({'get': 'retrieve', 'put': 'update'}),
        name='get-update')
]
