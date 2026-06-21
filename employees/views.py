
from django.db import transaction

from rest_framework.views import APIView
from accounts.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from setup.models import Role
from employees.models import Employee
from accounts.models import User

from employees.validation.validation_employee import validate_employee_create


class EmployeeCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:
            employee_account_data, employee_profile_data, json_error = (
                validate_employee_create(request.data)
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

            with transaction.atomic():

                user = User.objects.create_user(
                    email=employee_account_data["email"],
                    username=employee_account_data["username"],
                    password=employee_account_data["username"],
                    role_id=employee_account_data["role_id"]
                )

                employee = Employee.objects.create(
                    user=user,
                    first_name=employee_profile_data["first_name"],
                    middle_name=employee_profile_data["middle_name"],
                    last_name=employee_profile_data["last_name"],
                    created_by=request.user
                )

            return Response(
                {
                    "success": True,
                    "message": "Employee created successfully",
                    "data": {
                        "id": employee.id,
                        "employee_name": (
                            f"{employee.first_name} "
                            f"{employee.last_name}"
                        ),
                        "email": user.email
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
class EmployeeListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        employees = Employee.objects.filter(is_void=False)

        data = [
            {
                "id": employee.id,
                "first_name": employee.first_name,
                "middle_name": employee.middle_name,
                "last_name": employee.last_name,
                "email": employee.user.email,
                "role": employee.user.role.role_name
                if employee.user.role else None
            }
            for employee in employees
        ]

        return Response(
            {
                "success": True,
                "message": "Employee list fetched successfully",
                "data": data
            }
        )
        

class EmployeeDeleteView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, employee_id):

        try:

            with transaction.atomic():

                employee = Employee.objects.get(
                    id=employee_id,
                    is_void=False
                )

                employee.is_void = True
                employee.save(
                    update_fields=["is_void"]
                )

            return Response(
                {
                    "success": True,
                    "message": "Employee deleted successfully"
                }
            )

        except Employee.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Employee not found"
                },
                status=status.HTTP_404_NOT_FOUND
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