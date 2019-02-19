from django.urls import path ,include

from . import views
# link my url

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('polls.url'))
]