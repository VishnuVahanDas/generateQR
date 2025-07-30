from django.urls import path
from . import views

app_name = 'qr'

urlpatterns = [
    path('', views.create_qr, name='create'),
    path('<int:pk>/', views.qr_detail, name='detail'),
]
