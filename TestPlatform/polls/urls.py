from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('<int:question_id>/',views.detail,name="detail"),
    path('<int:question_id>/results/',views.results,name="result"),
    path('<int:question_id>/vote',views.vote,name="vote")
]