from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, status
from .models import CustomRoles
from .serializers import CustomRolesSerializer
from rest_framework.permissions import AllowAny

class MyTokenObtainPairView(TokenObtainPairView):
    pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    return Response({'username': user.username, 'role': user.role})

class RegisterUserView(generics.CreateAPIView):
    queryset = CustomRoles.objects.all()
    serializer_class = CustomRolesSerializer
    permission_classes = [AllowAny]

class ListUsersView(generics.ListAPIView):
    queryset = CustomRoles.objects.all()
    serializer_class = CustomRolesSerializer
    permission_classes = [IsAdminUser]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomRoles.objects.all()
    serializer_class = CustomRolesSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def update_view_both_access(request, pk):
    print(f"Received PATCH request for user ID: {pk}")
    try:
        user = CustomRoles.objects.get(pk=pk)
        print(f"User found: {user.username}")
    except CustomRoles.DoesNotExist:
        print("User not found!")
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user.can_view_both = True
    user.save()
    print(f"Updated user {user.username} to view both.")
    return Response({"message": f"User {user.username} can now view both male and female data"}, status=status.HTTP_200_OK)
