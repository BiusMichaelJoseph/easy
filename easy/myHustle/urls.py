
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('userAuth.urls')),
    path('api/profile/', include('userProfile.urls')),
    path('api/mediaInteractions/', include('mediaInteractions.urls')),
]
