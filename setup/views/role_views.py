from django.db import transaction
from rest_framework.views import APIView
from django.shortcuts import render

from setup.validation import validate_role_create
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsPermission
from rest_framework.response import Response
from rest_framework import status
from setup.models import Role


class DepartmentListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return render(request, "department/department_list.html")


class RoleListView(APIView):

    permission_classes = [IsPermission]

    def get(self, request):

        roles = Role.objects.filter(status="active")

        data = [
            {
                "id": role.id,
                "role_name": role.role_name,
                "status": role.status
            }
            for role in roles
        ]

        return Response({
            "message": "Role list",
            "data": data
        })


class RoleCreateView(APIView):
    permission_menu = "Roles"

    permission_classes = [IsPermission]

    def post(self, request):

        try:
            with transaction.atomic():

                role_name, role_status, json_error = validate_role_create(
                    request.data
                )

                if json_error:
                    return Response(
                        {
                            "success": False,
                            "message": "Validation failed",
                            "errors": json_error
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

                role = Role.objects.create(
                    role_name=role_name,
                    status=role_status
                )

                return Response(
                    {
                        "success": True,
                        "message": "Role created successfully",
                        "data": {
                            "id": role.id,
                            "role_name": role.role_name,
                            "status": role.status
                        }
                    },
                    status=status.HTTP_201_CREATED
                )

        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": "Internal server error",
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )