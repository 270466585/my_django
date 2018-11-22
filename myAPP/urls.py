from django.conf.urls import url
from . import views

app_name='myAPP'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
    url(r'^(?P<username>[A-Za-z0-9]+)/createUser',views.createUser,name='createUser'),
    url(r'^(?P<question_id>[0-9]+)/detail',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/detail_test',views.detail_test,name='detail_test'),
    url(r'^specifics/(?P<question_id>[0-9]+)/detail_tests',views.detail_tests,name='detail_tests'),
]