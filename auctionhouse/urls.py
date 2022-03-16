from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from auctions import views as auctions_views

urlpatterns = [
    path('', auctions_views.index, name="index"),
    path('myauctions/', auctions_views.my_auctions, name="my_auctions"),
    path('mybids/', auctions_views.my_bids, name="my_bids"),
    path('auctions/', include('auctions.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/register", views.register, name="register"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
