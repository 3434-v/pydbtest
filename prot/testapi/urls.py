from django.urls import path
from . import views

app_name = 'testapi'
urlpatterns = [
    path('readim', views.readim, name='readim'),

]