from django.contrib import admin
from django.urls import path, include
from .views import CustomUserAuthToken

from dj_rest_auth.registration import views as reg_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('token/', CustomUserAuthToken.as_view(),  name="rest_login"),
    path('signup/', reg_views.RegisterView.as_view()),
    path('game/', include('game.urls')),
]
