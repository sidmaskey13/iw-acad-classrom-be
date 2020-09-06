from django.urls import path,include

from all_apps.apis.authentication import RegisterAPI, LoginAPI, UserAPI,RegisterStaffAPI, AllUserAPI
from knox import views as knox_views
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/register_staff', RegisterStaffAPI.as_view()),
    path('api/auth/all_users/', AllUserAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(),name='knox-logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)