from django.urls import include, path
from users.views import dashboard, register
from django.views.generic import RedirectView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('oauth/', include('social_django.urls')),
    path('register/', register, name='register'),
]