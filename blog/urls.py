from django.urls import path
from . import views

# show post_list on income
urlpatterns = [
    path('', views.post_list, name='post_list'),
]