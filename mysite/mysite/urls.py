from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('vietnam/', include('vietnam.urls')),

    path('api-auth', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
]
