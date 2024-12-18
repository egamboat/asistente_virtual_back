from django.urls import path
from .views import GoogleLoginView,CustomTokenRefreshView,DeleteAccountView, SolicitudAyudaView

urlpatterns = [
    path("api/google-login/", GoogleLoginView.as_view(), name='google-login'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/delete-account/', DeleteAccountView.as_view(), name='delete_account'),
    path('solicitudes/', SolicitudAyudaView.as_view(), name='solicitudes'),
]
