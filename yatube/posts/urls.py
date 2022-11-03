from django.urls import path


from . import views


urlpatterns = [
    path('', views.index),
    path('group/<slug:gk>/', views.group_posts),
]