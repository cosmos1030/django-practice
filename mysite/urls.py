from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('practice/', include('practice.urls')),
    path('hello/', include('hello.urls')),
]