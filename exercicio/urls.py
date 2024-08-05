from django.urls import path
from exercicio import views

urlpatterns = [
    path('natalia/', views.natalia_view, name='natalia'),
]
