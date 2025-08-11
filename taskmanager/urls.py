# taskmanager/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView
from tasks.views import RegisterView, UserDetailView
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Your app's main API routes
    path('api/', include('tasks.urls')),
    path('api/auth/register/', RegisterView.as_view(), name='auth_register'),
    # Authentication Routes
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/me/', UserDetailView.as_view({'get': 'retrieve'}), name='user-detail'),
    # Frontend catch-all (put this last)
    path('', TemplateView.as_view(template_name='index.html')),
]

# urlpatterns += [
#     re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
# ]
    
    