from django.urls import path
import apps.users.views as user_views

urlpatterns = [
    path("login/", user_views.LoginUserAPI.as_view(), name='login-user'),
    path("logout/", user_views.LogoutUserAPI.as_view(), name='logout-user'),
    path('refresh-token/',user_views.RefreshTokenAPI.as_view(), name='get-refresh-token'),
    path("signup/", user_views.CreateUserAPI.as_view(), name='signup-user'),
    path("update-profile/", user_views.UpdateUserAPI.as_view(), name='update-profile'),
    path("details/", user_views.GetUserDetailAPI.as_view(), name='update-profile')
]
