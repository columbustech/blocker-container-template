from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('block/', views.BlockView.as_view()), 
    path('admin/', admin.site.urls),
]
