from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='firetek/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='firetek/logout.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)