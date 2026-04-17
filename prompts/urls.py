from django.urls import path
from . import views

urlpatterns = [
    path('', views.prompt_list),
    path('<int:id>/', views.prompt_detail),
]