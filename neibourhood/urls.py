from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$', views.homepage, name='homepage'),
    url(r'^add/hood$', views.add_hood, name='add_hood'),
    url(r'^add/biz$', views.add_biz, name='add_biz'),
    url(r'^add/post$', views.add_post, name='add_post'),
    url(r'^search_results/', views.search_results, name='search_results')
    url(r'^user/(?P<username>\w+)', views.user_profile, name='user_profile')
]