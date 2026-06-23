from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.permissions import IsPermission
from setup.models import MenuRole
from rest_framework import status

from setup.validation import validate_menu_role_create


class MenuRoleListView(APIView):

    permission_classes = [IsPermission]
    permission_menu = "Menu Role"

    def get(self, request):

        menu_roles = MenuRole.objects.select_related("role").all()

        data = [
            {
                "id": mr.id,
                "role": mr.role.role_name,
                "menu": mr.menu,
                "view": mr.is_view,
                "add": mr.is_add,
                "edit": mr.is_edit,
                "delete": mr.is_delete,
            }
            for mr in menu_roles
        ]

        return Response({
            "message": "MenuRole list",
            "data": data
        })
        

class MenuRoleCreateView(APIView):

    permission_classes = [IsPermission]
    permission_menu = "Menu Role"

    def post(self, request):

        try:
            with transaction.atomic():
                
                menu_role_data, json_error = validate_menu_role_create(
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

                menu_role = MenuRole.objects.create(
                    role_id= int(menu_role_data["role_id"]),
                    menu= menu_role_data["menu"],
                    is_view = menu_role_data["is_view"],
                    is_add= menu_role_data["is_add"],
                    is_edit= menu_role_data["is_edit"],
                    is_delete= menu_role_data["is_delete"],
                    created_by=request.user
                )

                return Response({
                    "success": True,
                    "message": "MenuRole created successfully",
                    "data": {
                        "id": menu_role.id,
                        "role": menu_role.role_id,
                        "menu": menu_role.menu
                    }
                }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                "success": False,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)