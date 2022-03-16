from django.urls import path

from . import views
app_name = 'auctions'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.auctions, name='auctions'),
    path('<int:auction_id>/', views.detail, name='detail'),
    path('<int:auction_id>/bid/', views.bid, name='bid'),
]
