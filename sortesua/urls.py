from django.urls import path
from . import views

urlpatterns = [
    path("", views.aposta_index, name="aposta_index"),
    # path("<int:pk>/", views.aposta_detail, name="aposta_detail"),
]