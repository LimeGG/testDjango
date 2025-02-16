from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls'), name="home"),
                  path('lkusers/', include('lkusers.urls')),
                  path('registration/', include('registration.urls')),
                  path('shop/', include('shop.urls')),
                  path('streamers/', include('streamers.urls')),
                  path("api/", include("apiv.urls"))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
