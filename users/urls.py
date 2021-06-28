from django.urls import include, path
from users.views import dashboard, register
from django.views.generic import RedirectView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard', RedirectView.as_view(url = 'dashboard/')),
    path('dashboard/', dashboard, name='dashboard'),
    path('oauth/', include('social_django.urls')),
    path('register/', register, name='register'),
]