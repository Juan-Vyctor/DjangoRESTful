from django.urls import path
from toys import views

urlpatterns = [
    path('list/',views.toy_list),
    path('details/<int:pk>/', views.toy_detail),
]