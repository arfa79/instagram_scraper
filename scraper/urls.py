from django.urls import path
from . import views

urlpatterns = [
    path('influencer/<str:username>/', views.influencer_detail, name='influencer_detail'),
]