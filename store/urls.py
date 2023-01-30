from . import views
from django.urls import path

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail'),

    ]