from django.conf.urls import url

from . import views

urlpatterns = [
    #ex: /tngs_results/
    url(r'^$', views.post_list, name='index'),
    #ex: /tngs_results/patient_id/
    #url(r'^(?P<patient_id>patient\d)/$', views.detail, name='detail'),
]


