from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),        # /polls/
    path('<int:question_id>/', views.detail, name='detail'),        # /polls/11/
    path('<int:question_id>/results/', views.results, name='results'),      # /polls/11/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),       # /polls/11/vote/
]
