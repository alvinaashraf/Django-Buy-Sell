
from django.contrib import admin
from django.urls import path,include
from core.views import index, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls'),name='index'),
    path('inbox/',include('conversation.urls')),
    path('item/' , include('item.urls')),
    path('dashboard/',include('dashboard.urls'))
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
