from django.urls import path
from .views import (
    MyTokenObtainPairView,
    user_profile,
    RegisterUserView,
    ListUsersView,
    UserDetailView,
    update_view_both_access
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', user_profile, name='user_profile'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('users/', ListUsersView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/view-both/', update_view_both_access, name='update_view_both_access')
]
