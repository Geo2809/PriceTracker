from django.urls import path
from . import views
urlpatterns = [
    path('',  views.home_view, name='home'),
    path('delete/<pk>/',  views.LinkDeleteView.as_view(), name='delete'),
    path('update/',  views.update_prices, name='update-prices'),
]