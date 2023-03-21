from . import views
from django.urls import path


app_name = 'todo'

urlpatterns = [
    path('', views.PostList.as_view(), name="index,"),
    path('ag/', views.ag, name="ag"),
    path('spesso/', views.ag, name="spesso"),
    path('sushisho/', views.ag, name="sushisho"),
]
