from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^skill/list/$', views.skill_list, name='skill_list'),
]
