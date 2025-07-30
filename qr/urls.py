from django.urls import path
from . import views

app_name = 'qr'

urlpatterns = [
    path('', views.create_qr, name='create'),
    path('mine/', views.user_qr_list, name='my_qrs'),
    path('<int:pk>/', views.qr_detail, name='detail'),
]
