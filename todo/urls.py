from . import views
from django.urls import path


app_name = 'todo'

urlpatterns = [
    path('', views.PostList.as_view(), name="index"),
]