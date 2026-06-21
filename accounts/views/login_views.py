from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


from django.http import JsonResponse
from django.middleware.csrf import get_token


def csrf_token_view(request):
    return JsonResponse({
        "csrfToken": get_token(request)
    })
    
class LoginAPIView(APIView):

    permission_classes = []

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username=email, password=password)

        if user is None:
            return Response({
                "message": "Invalid email or password"
            }, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)

        return Response({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username
            }
        })

class LogoutAPIView(APIView):

    def post(self, request):
        logout(request)

        return Response({
            "message": "Logout successful"
        })