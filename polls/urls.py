from django.contrib import admin

from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.owner, name='owner'),
    path('owner', views.owner, name='owner'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
