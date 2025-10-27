from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),                    # homepage
    path('<str:short_code>/', views.redirect_url, name='redirect'),  # redirect route
]
