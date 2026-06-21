from django.urls import path
from .views import *

urlpatterns = [
    path("api/employees/list/", EmployeeListView.as_view(), name="employees_list"),
    path( "api/employees/create/",EmployeeCreateView.as_view(),name="employees_create"),
    path("api/employees/<int:employee_id>/", EmployeeDeleteView.as_view(),name="employee_delete"),
]