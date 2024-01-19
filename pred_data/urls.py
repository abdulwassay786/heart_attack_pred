from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.heart_data, name = 'heart_data'),
    path('success/<int:pk>/', views.success_page, name = 'success_page')
]
