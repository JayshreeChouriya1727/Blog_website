
from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),# this path redirect to the views.py file of this app
   
    path('<slug:post>/',views.post_single,name='post_single'), # each one have different different post it also redirect views.py file and point post_sinngle function

    path('category/<category>/',views.CatListView.as_view(), name='category'),# redirect to the views.py file and point to catlistView function.
   
]
