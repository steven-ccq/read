from django.conf.urls import url
from django.urls import path, include
from .views import *
from experiments import views
app_name = 'experiments'
urlpatterns = [
    path('center/<int:page>/',views.allbookpage, name='allbookpage'),
    path('detail/<int:id>/<int:page>/',views.detail, name='detail'),
]